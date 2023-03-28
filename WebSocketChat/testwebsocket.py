import pytest
from websocket import create_connection
import websocket

class TestDyd():
    url = "ws://localhost:12230"

    @classmethod
    def setup_class(cls):
        cls.ws = create_connection(cls.url)  # 建立连接
        cls.ws.settimeout(5)  # 设置超时时间

    def test_connect(self):
        # 通过状态码判断连接是否正常
        assert self.ws.getstatus() == 101

    def test_send(self):
        params = {"code":1,"data":{"heartbeat":"Heartbeat"},"timestamp":2088751475875914}  			# 定义传参

        self.ws.send(params)			# 发送请求
        result = self.ws.recv()			# 获取响应结果
        print("收到来自服务端的消息：", result)	# 打印响应结果
        # 因为该测试项目传参会显示在响应中，所以通过判断传参是否在响应结果中进行断言
        assert params in result

if __name__ == '__main__':
    pytest.main(["-vs"])
