import logging
from logging import getLogger


class LogUtils:
    @classmethod
    def get_logger(cls) -> logging:
        """
        无需实现
        :return:
        """
        return getLogger(__name__)

    @classmethod
    def register_get_logger(cls, func) -> logging:
        cls.get_logger = func
        return func
