class CacheUtils:
    """
    全局缓存类
    """

    @classmethod
    def set(cls, key: str, value: str, expire=None):
        """
        设置一个缓存,scope=plugin
        :param key: 缓存的key
        :param value: 缓存的值
        :param expire: 缓存过期时间,为空的代表永久,单位毫秒
        :return:
        """
        ...

    @classmethod
    def get(cls, key: str, default=None) -> str:
        """
        获取一个缓存,scope=plugin
        :param key: 缓存的key
        :param key: 默认值
        :return: 缓存的内容,nullable
        """
        ...

    @classmethod
    def key_exists(cls, key: str) -> bool:
        """
        判断key是否存在,scope=plugin
        :param key: 缓存的key
        :return: 缓存是否存在
        """

    @classmethod
    def register_set(cls, func):
        """
        注册一个设置缓存的函数
        :param func: 函数,参数为key,value,expire
        :return:
        """
        cls.set = func
        return func

    @classmethod
    def register_get(cls, func):
        """
        注册一个获取缓存的函数
        :param func: 函数,参数为key
        :return:
        """
        cls.get = func
        return func

    @classmethod
    def register_key_exists(cls, func):
        """
        注册一个判断key是否存在的函数
        :param func: 函数,参数为key
        :return:
        """
        cls.key_exists = func
        return func
