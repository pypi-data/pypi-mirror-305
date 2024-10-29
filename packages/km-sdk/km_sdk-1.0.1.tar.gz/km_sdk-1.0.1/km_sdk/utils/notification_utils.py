from strenum import StrEnum
from ..api_provider import ApiProvider

class FileChangeType(StrEnum):
    """
    文件变动类型
    """

    """
    当文件权限发生变动
    """
    FILE_PERMISSION = "file.permission"

    """
    当文件内容发生变动
    """
    FILE_EDIT = "file.edit"

    """
    当文件被删除时
    """
    FILE_DELETE = "file.delete"
    """
    当文件新增时
    """
    FILE_ADD = "file.add"


class SystemNotificationUtils:
    """
    事件通知
    """

    @classmethod
    def file_change(cls, api_provider: ApiProvider, file_change_type: FileChangeType, file_id: str):
        """
        当文件发生变动时通知系统,无需实现
        :param api_provider 传入 api_provider
        :param file_change_type: 文件变动类型 see FileChangeType
        :param file_id: 文件ID
        :return:
        """
        ...

    @classmethod
    def register_file_change(cls, func):
        cls.file_change = func
        return func
