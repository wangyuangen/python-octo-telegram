# -*- coding: utf-8 -*-
import sys
sys.path.append('../FormFile')
reload(sys);
sys.setdefaultencoding('utf8');
from LogicEvent import *
from Logon import Ui_LogOn          #引用Logon窗体
from Register import Ui_register_2  #引用register窗体
from Main import Ui_MainForm        #引用main窗体
from PyQt4 import QtCore, QtGui

app = QtGui.QApplication(sys.argv)
logon = Ui_LogOn()
main = Ui_MainForm()

if __name__ == "__main__":
    logonEve = logonEvent(logon,main)                     #logon事件
    register = Ui_register_2()                            #register窗体实例
    registerEve = registerEvent(register)                 #register事件
    register.pb_register.clicked.connect(registerEve.reg)  #给注册按钮一个点击事件,该点击事件触发registerEve.reg
    logon.pb_logon.clicked.connect(logonEve.loggon)        #给登录按钮一个点击事件,该点击事件触发logonEve.loggon
    logon.show()                                #登录窗体显示
    logon.le_account.editingFinished.connect(logonEve.getHeadImg)   #登录窗体账号文本框修改结束时触发logonEve.getHeadImg
    logon.pb_register.clicked.connect(register.show)        #点击立即注册时打开注册窗体
    sys.exit(app.exec_())                                   #等候退出