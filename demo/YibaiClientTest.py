# encoding=utf8

import json
from yibai.api import *

server_url = 'https://sms.100sms.cn/api'
#此处为你的apikey，可登录https://web.100sms.cn/ 查看你的apikey
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
