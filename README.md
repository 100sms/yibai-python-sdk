# yibai-python-sdk
The python sdk of https://www.100sms.cn/

 - 模块安装
 ```
 1. 将yibai-sms-python-sdk-1.0.0文件夹添加到python安装目录
 2. 进入该文件夹下执行：python setup.py install
 ```

 - 代码调用示例
 
```python
# encoding=utf8

import json
from yibai.api import *

server_url = 'https://sms.100sms.cn/api'
#此处为你的apikey，可登录web.100sms.cn 查看你的apikey
apikey = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
client = YibaiClient(server_url, apikey)


def test_sms_batch_submit():
    try:
        response = client.sms_batch_submit([
            {'mobile': '187xxxxxxxx', 'message': '【亿佰云通讯】您的验证码是：1234'},
            {'mobile': '186xxxxxxxx', 'message': '【亿佰云通讯】您的验证码是：5678'}
        ])
        print json.dumps(response)
    except YibaiApiError as e:
        print 'YibaiApiError. code: {0}, message: {1}'.format(e.code, e.message.encode('utf8'))
    except Exception as e:
        print 'Unexpected error. ' + e.message


def test_sms_pull_status_report():
    try:
        response = client.sms_pull_status_report()
        print json.dumps(response)
    except YibaiApiError as e:
        print 'YibaiApiError. code: {0}, message: {1}'.format(e.code, e.message.encode('utf8'))
    except Exception as e:
        print 'Unexpected error.' + e.message


def test_sms_pull_reply_message():
    try:
        response = client.sms_pull_reply_message()
        print json.dumps(response)
    except YibaiApiError as e:
        print 'YibaiApiError. code: {0}, message: {1}'.format(e.code, e.message.encode('utf8'))
    except Exception as e:
        print 'Unexpected error.' + e.message


test_sms_pull_reply_message()

```
# 注意事项
 - demo中的PythonSmsApiSample.py为非sdk调用示例,仅供测试接口,实际使用推荐sdk调用
 - 详细api文档请参考https://www.100sms.cn/api1.0/document
