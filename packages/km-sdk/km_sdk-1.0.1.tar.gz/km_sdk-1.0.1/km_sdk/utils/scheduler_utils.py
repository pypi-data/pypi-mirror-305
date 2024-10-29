from apscheduler.triggers.base import BaseTrigger


class SchedulerUtils:
    """
    定时任务相关工具
    """

    @classmethod
    def add_job(cls, id, trigger: BaseTrigger, func: callable, **kwargs):
        """
        添加定时任务
        :param id: 任务唯一ID
        :param trigger: 执行频率
        :param func: 执行函数
        :param kwargs: 执行参数
        :return:
        """
        ...

    @classmethod
    def remove_job(cls, job_id):
        """
        移除定时任务
        :param job_id: 任务ID
        :return:
        """
        ...

    @classmethod
    def register_add_job(cls, func):
        """

        :param func:
        :return:
        """
        cls.add_job = func
        return func

    @classmethod
    def register_remove_job(cls, func):
        """

        :param func:
        :return:
        """
