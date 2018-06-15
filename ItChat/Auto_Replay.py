#coding=utf8
from itchat.content import *
import requests
import json
import itchat

itchat.auto_login(hotReload = True)

def tuling(info):
    appkey = "e5ccc9c7c8834ec3b08940e290ff1559"
    url = "http://www.tuling123.com/openapi/api?key=%s&info=%s"%(appkey,info)
    req = requests.get(url)
    content = req.text
    data = json.loads(content)
    answer = data['text']
    return answer


def group_id(name):
    df = itchat.search_chatrooms(name=name)
    return df[0]['UserName']

@itchat.msg_register([TEXT,MAP,CARD,NOTE,SHARING])
def text_reply(msg):
    itchat.send('%s' % tuling(msg['Text']),msg['FromUserName'])

@itchat.msg_register([PICTURE, RECORDING, ATTACHMENT, VIDEO])
def download_files(msg):
    msg['Text'](msg['FileName'])
    return '@%s@%s' % ({'Picture': 'img', 'Video': 'vid'}.get(msg['Type'], 'fil'), msg['FileName'])

@itchat.msg_register(TEXT, isFriendChat=True,isGroupChat=True,isMpChat=True)
def group_text_reply(msg):
    item = group_id('damn')
    if msg['ToUserName'] == item:
        itchat.send(u'%s' % tuling(msg['Text']), item)

itchat.run()
