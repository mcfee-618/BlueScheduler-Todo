import abc
from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.request import CommonRequest


class MessageSdk:
    @abc.abstractmethod
    def send_message(self, phonenumber: str, message: str):
        pass


class AliyunMessageSdk(MessageSdk):
    def __init__(self, **params):
        client = AcsClient(params.get("accessKeyId"), params.get("accessSecret"), 'ap-northeast-1')
        self.client = client

    def send_message(self, phonenumber: str, message: str):
        request = CommonRequest()
        request.set_accept_format('json')
        request.set_domain('dysmsapi.aliyuncs.com')
        request.set_method('POST')
        request.set_protocol_type('https')
        request.set_version('2017-05-25')
        request.set_action_name('SendSms')
        request.add_query_param('PhoneNumbers', phonenumber)
        request.add_query_param('SignName', "阿里大于测试专用")
        request.add_query_param('TemplateCode', "SMS_209335004")
        request.add_query_param('TemplateParam', "{\"code\":\"1111\"}")
        response = self.client.do_action(request)
        print(response)


if __name__ == "__main__":
    aliyun_sdk = AliyunMessageSdk(accessKeyId="LTAI5tGQfSP5gu9oydrydsEs", accessSecret="VY6sC3TFPjxgAddB9CGmr1VqZ9nzrs")
    aliyun_sdk.send_message("13552900618","test1")
