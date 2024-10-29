import json
from collections.abc import Callable

from ..api_provider import ApiProvider


class WebhookUtils:
    @classmethod
    def add_webhook(cls, api_provider: ApiProvider, url: str, methods: [str], handler: Callable[..., dict],
                    endpoint: str = None) -> str:
        """
        注册一个webhook,webhook需要自己做权限验证
        :param api_provider: 插件实例
        :param url:最终网址是 http(s)://域名/v1/webhook/{插件唯一ID}/{url}
            url 可以通过<id> 来接收参数,必须要在处理函数接收id参数
        :param methods: 可以接受的方法
        :param handler: 处理参数的函数,必须可以通过callable()检查,handler 应该返回3个参数分别是 status_code,content-type,和body
        :param endpoint: 网址名称
        :return:返回注册的url
        """
        return ""

    @classmethod
    def get_request_header(cls) -> dict | None:
        """
        获取请求头
        :return:
        """
        return None

    @classmethod
    def get_request_json(cls) -> dict | None:
        """
        获取请求体
        :return:
        """
        return None

    @classmethod
    def get_request_params(cls) -> dict | None:
        """
        获取请求参数
        :return:
        """
        return None

    @classmethod
    def get_request_form(cls) -> dict | None:
        """
        获取请求表单
        :return:
        """
        return None

    @classmethod
    def get_request_files(cls) -> dict | None:
        """
        获取请求上传的文件
        :return:
        """
        return None

    @classmethod
    def get_user_info(cls) -> dict:
        """
        获取登录用户
        """
        return {"id": "test_user_id", "name": "test_user_name"}

    @classmethod
    def add_response_header(cls, key: str, value: str) -> None:
        return None

    @classmethod
    def register_add_webhook(cls, func):
        """
        注册处理函数,无需实现
        :param func:
        :return:
        """
        cls.add_webhook = func
        return func


if __name__ == '__main__':
    def d(api_provider, *args, **kwargs):
        return 200, "application/json", json.dumps(
            {"text": "hello",
             "header": WebhookUtils.get_request_header(),
             "body": WebhookUtils.get_request_json(),
             "files": WebhookUtils.get_request_file().keys(),
             "params": WebhookUtils.get_request_params(),
             "form": WebhookUtils.get_request_form()
             })


    api_provider = ApiProvider()

    register_url = WebhookUtils.add_webhook(api_provider=api_provider,
                                            endpoint="/test",
                                            methods=["GET", "POST"],
                                            handler=d)
