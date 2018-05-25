# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'G:\PyProject\FormFile\Logon.ui'
#
# Created: Thu May 24 11:02:38 2018
#      by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_LogOn(QtGui.QMainWindow):
    def __init__(self):
        super(Ui_LogOn, self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)

    def setupUi(self, LogOn):
        LogOn.setObjectName(_fromUtf8("LogOn"))
        LogOn.resize(483, 211)
        LogOn.setStyleSheet(_fromUtf8("#QDialog{background-clor:red}"))
        self.le_account = QtGui.QLineEdit(LogOn)
        self.le_account.setGeometry(QtCore.QRect(190, 40, 191, 31))
        self.le_account.setObjectName(_fromUtf8("le_account"))
        self.le_pwd = QtGui.QLineEdit(LogOn)
        self.le_pwd.setGeometry(QtCore.QRect(188, 91, 191, 31))
        self.le_pwd.setObjectName(_fromUtf8("le_pwd"))
        self.pb_logon = QtGui.QPushButton(LogOn)
        self.pb_logon.setGeometry(QtCore.QRect(210, 150, 151, 31))
        self.pb_logon.setObjectName(_fromUtf8("pb_logon"))
        self.lb_headImg = QtGui.QLabel(LogOn)
        self.lb_headImg.setGeometry(QtCore.QRect(40, 40, 110, 90))
        self.lb_headImg.setObjectName(_fromUtf8("lb_headImg"))
        self.pb_register = QtGui.QPushButton(LogOn)
        self.pb_register.setGeometry(QtCore.QRect(390, 50, 75, 23))
        self.pb_register.setObjectName(_fromUtf8("pb_register"))
        self.pb_findPwd = QtGui.QPushButton(LogOn)
        self.pb_findPwd.setGeometry(QtCore.QRect(390, 90, 75, 23))
        self.pb_findPwd.setObjectName(_fromUtf8("pb_findPwd"))

        self.retranslateUi(LogOn)
        QtCore.QMetaObject.connectSlotsByName(LogOn)

    def retranslateUi(self, LogOn):
        LogOn.setWindowTitle(_translate("LogOn", "登录", None))
        self.pb_logon.setText(_translate("LogOn", "登录", None))
        self.lb_headImg.setText(_translate("LogOn", "", None))
        self.pb_register.setText(_translate("LogOn", "立即注册", None))
        self.pb_findPwd.setText(_translate("LogOn", "找回密码", None))

