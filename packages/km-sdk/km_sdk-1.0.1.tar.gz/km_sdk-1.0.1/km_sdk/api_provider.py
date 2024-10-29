from abc import ABCMeta, abstractmethod
from collections.abc import Iterable
from dataclasses import dataclass

from elasticsearch_dsl.query import Query
from .utils.files_utils import FileUtils

class BaseType:
    def to_dict(self):
        return dict([(k.lstrip("_"), v) for k, v in self.__dict__.items()])

    def to_dict_with_type(self):
        def _dict(obj):
            module = None
            if issubclass(obj.__class__, BaseType):
                data = {}
                for attr, v in obj.__dict__.items():
                    k = attr.lstrip("_")
                    data[k] = _dict(v)
                module = obj.__module__
            elif isinstance(obj, (list, tuple)):
                data = []
                for i, vv in enumerate(obj):
                    data.append(_dict(vv))
            elif isinstance(obj, dict):
                data = {}
                for _k, vv in obj.items():
                    data[_k] = _dict(vv)
            else:
                data = obj
            return {"type": obj.__class__.__name__,
                    "data": data, "module": module}

        return _dict(self)


class TreeNode(BaseType):
    #对象的唯一标识
    id: str = None
    #对象的名称
    name: str = None
    #对象的类型,如果对象是文件夹那么为文件夹的类型,比如知识库,云盘,空间,文件夹等,如果是文件,那么应该是文件的扩展名
    type: str = None
    #是否是文件
    is_file:bool=None



@dataclass
class FileDto(BaseType):
    def __init__(self, d):
        self.__dict__ = d

    id: str = None
    name: str = None
    size: str = None
    md5: str = None


@dataclass
class PermissionDto(BaseType):
    type: str
    value: [str]
    extend: str | None


@dataclass
class UserDto(BaseType):
    name: str
    id: str
    permissions: [PermissionDto]


class ApiProvider(BaseType, metaclass=ABCMeta):

    def __init__(self, *args, **kwargs):
        """
        初始化接受参数
        :param args:
        :param kwargs:
        """
        self.related_sync_system = kwargs.get("related_sync_system", None)
        ...

    def get_related_sync_system(self) -> str:
        return self.related_sync_system

    def fetch_file(self, **kwargs) -> Iterable[FileDto]:
        page_size = int(kwargs.get("page_size", 20))
        page = int(kwargs.get("page", 1))
        while True:
            files = self.get_files(page_size=page_size, current=page)
            if not files:
                break
            for file in files:
                yield file
            page = page + 1

    @abstractmethod
    def get_files(self, page_size=20, current=1) -> [FileDto]:
        """
        获取文件列表
        :param page_size: 每页条数
        :param current: 页数
        :return:
        """
        ...

    @abstractmethod
    def get_file(self, file_id: str) -> FileDto:
        """
        获取指定文件的详情
        :param file_id:
        :return:
        """
        ...

    @abstractmethod
    def download(self, file_id: str) -> bytes:
        """
        下载文件
        :param file_id:
        :return:
        """
        ...

    @abstractmethod
    def list_file_permission(self, file_id: str) -> [PermissionDto]:
        """
        获取文件的权限列表
        :param file_id:
        :return:
        """
        ...

    @abstractmethod
    def list_user_file_permission(self, user_id: str, file_ids: [str]) -> [str]:
        """
        测试用户是否有给定文件的权限
        :param user_id: 用户ID
        :param file_ids: 文件ID集合
        :return:
        """
        ...

    @abstractmethod
    def get_user(self, user_id: str) -> UserDto:
        """
        获取用户信息
        :param user_id:用户ID
        :return:
        """
        ...

    @abstractmethod
    def build_filter(self, user_id: str, related_sync_system: str, bqry: Query) -> Query:
        """
        根据用户权限获取查询条件
        :param user_id: 用ID
        :param related_sync_system: 关联系统标识
        :param bqry: es query查询对象
        :return:
        """
        ...

    def get_as_tree_node(self, file_id: str = None, file_type: str = None, next_page_token : str = None, page_size: int = 20):
        """
        {
        "files":
            [
                {
                    "id":"123123",
                    "name":"云盘",
                    "type":"cloud_driver",
                    "is_file":false
                },
                {
                    "id":"sdfsdfs",
                    "name":"知识库",
                    "type":"wiki",
                    "is_file":false
                },
                {
                    "id":"dsfsdfs",
                    "name":"钉盘",
                    "type":"oss",
                    "is_file":false
                }
            ],
        "next_page_token":null
        }
        :param file_id: 文件夹唯一ID
        :param file_type: 文件夹类型
        :param next_page_token:获取下一页的标识
        :param page_size:获取条数
        """

        raise NotImplementedError()

    def search_file(self, query: str,file_type: str=None):
        """
            [
                {
                    "id":"123123",
                    "name":"云盘",
                    "type":"cloud_driver",
                    "is_file":false
                },
                {
                    "id":"sdfsdfs",
                    "name":"知识库",
                    "type":"wiki",
                    "is_file":false
                },
                {
                    "id":"dsfsdfs",
                    "name":"钉盘",
                    "type":"oss",
                    "is_file":false
                }
            ]
        :param query: 查找的字符
        :param file_type: 查找的文件类型
        """
        raise NotImplementedError()
    @abstractmethod
    def system_init(self):
        """
        系统初始化的时候执行的方法,可以重载,也可以不重载
        """
        ...

    def system_unload(self):
        """
        系统删除的时候执行的方法,可以重载,也可以不重载
        """
        pass

    def test_connection(self):
        """
        测试连接是否正常,如果正常则返回None
        如果配置不正确则抛异常
        如果需要下一步操作则返回一个 GuideDTO
        默认正常
        :return:
        """
        return None

    def get_file_info(self, file):
        """
        获取文件信息,可以重载,也可以不重载 直接用
        :param file:
        :return:
        """
        content = self.download(file.id)
        with (FileUtils.write_temp_file(content) as temp):
            if file.size is None:
                file.size = FileUtils.file_size(temp.name)
            if not file.md5:
                file.md5 = FileUtils.file_md5(temp.name)

    @staticmethod
    def get_description() -> dict:
        """
        获取api描述信息
        like {
            "name": "鸿翼",
            "type": "ECM",
            "params": [
                {
                    "name": "Base URL",
                    "key": "base_url",
                    "remark": "鸿翼系统的网址,例如 http://www.baidu.com",
                    "required": True,
                    "type": "input",
                    "rules": [{"type": "url"}]
                },
                {
                    "name": "API Key",
                    "key": "token",
                    "remark": "鸿翼系统的登录token",
                    "required": True,
                    "type": "input"
                }
            ],
            "description":"插件描述用法,支持markdown"
        }
        :return:
        """
        raise NotImplementedError
