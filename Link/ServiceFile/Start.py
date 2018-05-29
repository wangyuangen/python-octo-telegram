# -*- coding: utf-8 -*-
import sys
sys.path.append('../FormFile')
from LogicEvent import *
from Logon import Ui_LogOn          #引用Logon窗体
from Register import Ui_register_2  #引用register窗体
from Main import Ui_MainForm        #引用main窗体
from Message import Ui_message
from PyQt4 import QtCore, QtGui

app = QtGui.QApplication(sys.argv)
logon = Ui_LogOn()
main = Ui_MainForm()

if __name__ == "__main__":
    message = Ui_message()
    register = Ui_register_2()                            #register窗体实例

    mainEve = mainEvent(main,message)
    registerEve = registerEvent(register)                 #register事件
    logonEve = logonEvent(logon,main)                     #logon事件
    messageEve = messageEvent(message,main)

    register.pb_register.clicked.connect(registerEve.reg)  #给注册按钮一个点击事件,该点击事件触发registerEve.reg

    logon.pb_logon.clicked.connect(logonEve.loggon)        #给登录按钮一个点击事件,该点击事件触发logonEve.loggon
    logon.le_account.editingFinished.connect(logonEve.getHeadImg)   #登录窗体账号文本框修改结束时触发logonEve.getHeadImg
    logon.pb_register.clicked.connect(register.show)        #点击立即注册时打开注册窗体
    logon.show()                                #登录窗体显示

    main.lv_customer.clicked.connect(mainEve.openMessage)

    message.pb_send.clicked.connect(messageEve.sendMessage)
    message.pb_cancel.clicked.connect(message.close)
    sys.exit(app.exec_())                                   #等候退出