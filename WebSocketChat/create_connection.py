import websocket


def on_open(ws):  # 定义用来处理打开连接的方法
    print("打开连接")


def on_message(ws, message):  # 定义用来监听服务器返回消息的方法
    print("监听到服务器返回的消息，：\n", message)


def on_error(ws, error):  # 定义用来处理错误的方法
    print("连接出现异常：\n", error)


def on_close(ws):  # 定义用来处理断开连接的方法
    print("关闭连接")


if __name__ == "__main__":
    websocket.enableTrace(True)  # 可选择开启跟踪，在控制台可以看到详细的信息
    ws = websocket.WebSocketApp("ws://192.168.2.44:18082/socket/wcs/station",cookie='station_mac=F4-4D-30-C9-C7-E8; SSO_IDT=eyJhbGciOiJIUzI1NiJ9.eyJyb2xlIjpbIm1hbmFnZXIiXSwidXNlci1pZGVudGlmaWVyIjoiYWRtaW4iLCJ1c2VybmFtZSI6ImFkbWluIiwiaWF0IjoxNjYyMzc4OTUxLCJleHAiOjE2NjI3Mzg5NTF9.OcFtXj8OCkV3msacsUg-qZJZkj_SA_cdGUFv2mfiXZQ',
                                on_open=on_open,
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)
    ws.run_forever()  # 调用run_forever方法，保持长连接
