from flask import Flask
import time
from flask import Flask, request, make_response
import hashlib
import json
import xml.etree.ElementTree as ET


app = Flask(__name__)
app.debug = True


@app.route('/')  # 默认网址
def index():
    return 'Index Page'


@app.route('/wx', methods=['GET', 'POST'])
def wechat_auth():  # 处理微信请求的处理函数，get方法用于认证，post方法取得微信转发的数据
    if request.method == 'GET':
        token = '你自己设置好的token'
        data = request.args
        signature = data.get('signature', '')
        timestamp = data.get('timestamp', '')
        nonce = data.get('nonce', '')
        echostr = data.get('echostr', '')
        s = [timestamp, nonce, token]
        s.sort()
        s = ''.join(s)
        if (hashlib.sha1(s).hexdigest() == signature):
            return make_response(echostr)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
