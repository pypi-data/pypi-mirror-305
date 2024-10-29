from functools import wraps


class LockUtils:

    @classmethod
    def lock(cls,key=None, timeout=0):
        def wrapper(func):
            @wraps(func)
            def inner(*args, **kwargs):
                return func(*args, **kwargs)

            return inner

        return wrapper

    @classmethod
    def register_lock(cls, func):
        cls.lock = func
        return func
