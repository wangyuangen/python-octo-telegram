#--encoding:utf-8-- #
import itchat
from itchat.content import TEXT

itchat.auto_login(True)

friendList = itchat.get_friends(update=True)[1:]
for friend in friendList:
    print u'昵称:'+friend['NickName'] +u' 备注:'+friend['RemarkName']
    print u'City:'+friend['City']
    print u'个性签名:'+friend['Signature']
    print '--------------------------------------------------'
# @itchat.msg_register(itchat.content.TEXT)
# def msg_reply(msg):
#     if msg['ToUserName']!='filehelper':
#         return
#     itchat.send(u'测试消息', 'filehelper')
# itchat.auto_login(hotReload=True)
# itchat.run()