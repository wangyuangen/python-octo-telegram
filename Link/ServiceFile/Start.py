# -*- coding: utf-8 -*-
import sys
sys.path.append('../FormFile')
reload(sys);
sys.setdefaultencoding('utf8');
from LogicEvent import *
from Logon import Ui_LogOn
from Register import Ui_register_2
from Main import Ui_MainForm
from PyQt4 import QtCore, QtGui

app = QtGui.QApplication(sys.argv)
logon = Ui_LogOn()
main = Ui_MainForm()

if __name__ == "__main__":
    logonEve = logonEvent(logon,main)
    register = Ui_register_2()
    registerEve = registerEvent(register)
    register.pb_register.clicked.connect(registerEve.reg)
    logon.pb_logon.clicked.connect(logonEve.loggon)
    logon.show()
    logon.le_account.editingFinished.connect(logonEve.getHeadImg)
    logon.pb_register.clicked.connect(register.show)
    sys.exit(app.exec_())