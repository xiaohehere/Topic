# -*- coding:utf-8 -*-

import io
import os
import shutil
import sys
import threading
import urllib
import json
import asyncJson
from http.server import HTTPServer, SimpleHTTPRequestHandler, ThreadingHTTPServer

ip = "localhost"   # 监听IP，配置项
port = 8804       # 监听端口，配置项
index_url = "http://%s:%d/views/index.html" % (ip, port)  # 监听主页url，配置项

# C:\Users\abc\AppData\Local\python  缓存目录，shit


class MyRequestHandler(SimpleHTTPRequestHandler):
    protocol_version = "HTTP/1.0"
    server_version = "PSHS/0.1"
    sys_version = "Python/3.7.x"
    target = "./"  # 监听目录，配置项

    def do_GET(self):
        if self.path.find("/json/") > 0:
            print(self.path)
            req = {"success": "true"}
            self.send_response(200)
            self.send_header("Content-type", "json")
            self.end_headers()
            with open(self.path, 'r', encoding="utf-8") as f:
                data = json.load(f)
                rspstr = json.dumps(data)
                self.wfile.write(rspstr.encode("utf-8"))

        else:
            SimpleHTTPRequestHandler.do_GET(self)

    def do_POST(self):
        if self.path == "/signin":
            print("postmsg recv, path right")
        else:
            print("postmsg recv, path error")
            data = self.rfile.read(int(self.headers["content-length"]))
            data = json.loads(data)
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            rspstr = "recv ok, data = "
            rspstr += json.dumps(data, ensure_ascii=False)
            self.wfile.write(rspstr.encode("utf-8"))


def HttpServer():
    try:
        server = HTTPServer((ip, port), MyRequestHandler)
        print("服务器监听地址： ", index_url)
        server.serve_forever()
    except KeyboardInterrupt:
        server.socket.close()


if __name__ == "__main__":
    # 开启线程，触发动态数据
    a = threading.Thread(target=asyncJson.loop)
    a.start()

    HttpServer()
