from ..api_provider import ApiProvider


class SettingUtils:
    """
    scope级别
        system:跨插件,可以在多个插件之间共享
        plugin:跨实例,可以在一个插件的多个实例之间共享
        instance:只有设置的实例可以读取到
    """

    @classmethod
    def get_system_setting(cls, key: str, default=None) -> str:
        """
        获取系统配置,scope=system
        :param key:配置名称
        :param default: 默认值
        :return:
        """
        return default

    @classmethod
    def get_setting(cls, api_provider: ApiProvider, key: str, default: str = None):
        """
        获取运行时配置,scope=instance
        :param api_provider: 插件实例
        :param key: 配置的key
        :param default: 如果key过期或者不存在返回的默认值
        :return:
        """
        return default

    @classmethod
    def set_setting(cls, api_provider: ApiProvider, key: str, value: str, expire: int = None):
        """
        设置运行时配置,scope=instance
        :param api_provider: 插件实例
        :param key: 配置key
        :param value: 配置的value
        :param expire: 配置的过期时间,默认永不过期
        :return:
        """
        pass

    @classmethod
    def remove_setting(cls, api_provider: ApiProvider, key: str):
        """
        删除运行时配置,scope=instance
        :param api_provider: 插件实例
        :param key: 配置key
        :return:
        """
        pass

    @classmethod
    def register_get_system_setting(cls, func):
        """
        注册处理函数,无需实现
        :param func:
        :return:
        """
        cls.get_system_setting = func
        return func

    @classmethod
    def register_get_setting(cls, func):
        """
        注册处理函数,无需实现
        :param func:
        :return:
        """
        cls.get_setting = func
        return func

    @classmethod
    def register_set_setting(cls, func):
        """
        注册处理函数,无需实现
        :param func:
        :return:
        """
        cls.set_setting = func
        return func

    @classmethod
    def register_remove_setting(cls, func):
        """
        注册处理函数,无需实现
        :param func:
        :return:
        """
        cls.remove_setting = func
        return func
