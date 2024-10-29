import hashlib
import tempfile
from contextlib import contextmanager


class FileUtils:

    @classmethod
    def file_md5(cls, file_path: str) -> str:
        ...

    @classmethod
    def file_size(cls, file_path: str) -> int:
        ...

    @classmethod
    def write_temp_file(cls, content):
        ...

    @classmethod
    def register_file_md5(cls, func):
        cls.file_md5 = func
        return func

    @classmethod
    def register_file_size(cls, func):
        cls.file_size = func
        return func

    @classmethod
    def register_write_temp_file(cls, func):
        cls.write_temp_file = func
        return func


@FileUtils.register_file_md5
def file_md5(file_path):
    """
    计算文件md5
    :param file_path 文件路径
    :return:
    """
    md5 = hashlib.md5()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            md5.update(chunk)
    return md5.hexdigest()


@FileUtils.register_file_size
def file_size(file_path):
    """
    获取文件大小
    """
    from pathlib import Path
    f = Path(file_path)
    return f.stat().st_size


@FileUtils.register_write_temp_file
@contextmanager
def write_temp_file(content):
    """
    临时文件
    :param content:二进制流
    :return:
    """
    with tempfile.NamedTemporaryFile(mode='wb+') as temp:
        temp.write(content)
        temp.seek(0)
        yield temp