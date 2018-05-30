# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\WorkSpace\����\Project\python-octo-telegram\Link\FormFile\Register.ui'
#
# Created: Wed May 30 13:42:37 2018
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

class Ui_register_2(QtGui.QMainWindow):
    def __init__(self):
        super(Ui_register_2, self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)

    def setupUi(self, register_2):
        register_2.setObjectName(_fromUtf8("register_2"))
        register_2.resize(307, 501)
        self.lb_accountName = QtGui.QLabel(register_2)
        self.lb_accountName.setGeometry(QtCore.QRect(60, 20, 54, 21))
        self.lb_accountName.setObjectName(_fromUtf8("lb_accountName"))
        self.lb_nickName = QtGui.QLabel(register_2)
        self.lb_nickName.setGeometry(QtCore.QRect(60, 100, 54, 21))
        self.lb_nickName.setObjectName(_fromUtf8("lb_nickName"))
        self.lb_sex = QtGui.QLabel(register_2)
        self.lb_sex.setGeometry(QtCore.QRect(60, 140, 54, 21))
        self.lb_sex.setObjectName(_fromUtf8("lb_sex"))
        self.lb_headImg = QtGui.QLabel(register_2)
        self.lb_headImg.setGeometry(QtCore.QRect(60, 180, 54, 21))
        self.lb_headImg.setObjectName(_fromUtf8("lb_headImg"))
        self.lb_fontColor = QtGui.QLabel(register_2)
        self.lb_fontColor.setGeometry(QtCore.QRect(60, 240, 51, 21))
        self.lb_fontColor.setObjectName(_fromUtf8("lb_fontColor"))
        self.lb_phone = QtGui.QLabel(register_2)
        self.lb_phone.setGeometry(QtCore.QRect(60, 302, 54, 21))
        self.lb_phone.setObjectName(_fromUtf8("lb_phone"))
        self.lb_address = QtGui.QLabel(register_2)
        self.lb_address.setGeometry(QtCore.QRect(60, 340, 54, 21))
        self.lb_address.setObjectName(_fromUtf8("lb_address"))
        self.lb_pwd = QtGui.QLabel(register_2)
        self.lb_pwd.setGeometry(QtCore.QRect(60, 382, 54, 16))
        self.lb_pwd.setObjectName(_fromUtf8("lb_pwd"))
        self.le_accountName = QtGui.QLineEdit(register_2)
        self.le_accountName.setGeometry(QtCore.QRect(120, 20, 113, 20))
        self.le_accountName.setObjectName(_fromUtf8("le_accountName"))
        self.le_nickName = QtGui.QLineEdit(register_2)
        self.le_nickName.setGeometry(QtCore.QRect(120, 100, 113, 20))
        self.le_nickName.setObjectName(_fromUtf8("le_nickName"))
        self.le_sex = QtGui.QLineEdit(register_2)
        self.le_sex.setGeometry(QtCore.QRect(120, 140, 113, 20))
        self.le_sex.setObjectName(_fromUtf8("le_sex"))
        self.le_headImg = QtGui.QLineEdit(register_2)
        self.le_headImg.setGeometry(QtCore.QRect(120, 180, 113, 20))
        self.le_headImg.setObjectName(_fromUtf8("le_headImg"))
        self.le_fontColor = QtGui.QLineEdit(register_2)
        self.le_fontColor.setGeometry(QtCore.QRect(120, 240, 113, 20))
        self.le_fontColor.setObjectName(_fromUtf8("le_fontColor"))
        self.le_phone = QtGui.QLineEdit(register_2)
        self.le_phone.setGeometry(QtCore.QRect(120, 302, 113, 20))
        self.le_phone.setObjectName(_fromUtf8("le_phone"))
        self.le_address = QtGui.QLineEdit(register_2)
        self.le_address.setGeometry(QtCore.QRect(120, 340, 113, 20))
        self.le_address.setObjectName(_fromUtf8("le_address"))
        self.le_pwd = QtGui.QLineEdit(register_2)
        self.le_pwd.setGeometry(QtCore.QRect(120, 380, 113, 20))
        self.le_pwd.setObjectName(_fromUtf8("le_pwd"))
        self.lb_confirmPwd = QtGui.QLabel(register_2)
        self.lb_confirmPwd.setGeometry(QtCore.QRect(60, 422, 54, 16))
        self.lb_confirmPwd.setObjectName(_fromUtf8("lb_confirmPwd"))
        self.le_confirmPwd = QtGui.QLineEdit(register_2)
        self.le_confirmPwd.setGeometry(QtCore.QRect(120, 420, 113, 20))
        self.le_confirmPwd.setObjectName(_fromUtf8("le_confirmPwd"))
        self.pb_register = QtGui.QPushButton(register_2)
        self.pb_register.setGeometry(QtCore.QRect(50, 460, 191, 31))
        self.pb_register.setObjectName(_fromUtf8("pb_register"))
        self.lb_custName = QtGui.QLabel(register_2)
        self.lb_custName.setGeometry(QtCore.QRect(60, 60, 54, 21))
        self.lb_custName.setObjectName(_fromUtf8("lb_custName"))
        self.lineEdit = QtGui.QLineEdit(register_2)
        self.lineEdit.setGeometry(QtCore.QRect(120, 60, 113, 20))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.pb_openFile = QtGui.QPushButton(register_2)
        self.pb_openFile.setGeometry(QtCore.QRect(120, 200, 61, 23))
        self.pb_openFile.setObjectName(_fromUtf8("pb_openFile"))
        self.pb_choiceColor = QtGui.QPushButton(register_2)
        self.pb_choiceColor.setGeometry(QtCore.QRect(120, 260, 61, 23))
        self.pb_choiceColor.setObjectName(_fromUtf8("pb_choiceColor"))

        self.retranslateUi(register_2)
        QtCore.QMetaObject.connectSlotsByName(register_2)

    def retranslateUi(self, register_2):
        register_2.setWindowTitle(_translate("register_2", "注册", None))
        self.lb_accountName.setText(_translate("register_2", "用户名", None))
        self.lb_nickName.setText(_translate("register_2", "昵称", None))
        self.lb_sex.setText(_translate("register_2", "性别", None))
        self.lb_headImg.setText(_translate("register_2", "头像", None))
        self.lb_fontColor.setText(_translate("register_2", "字体颜色", None))
        self.lb_phone.setText(_translate("register_2", "电话", None))
        self.lb_address.setText(_translate("register_2", "地址", None))
        self.lb_pwd.setText(_translate("register_2", "密码", None))
        self.lb_confirmPwd.setText(_translate("register_2", "确认密码", None))
        self.pb_register.setText(_translate("register_2", "立即注册", None))
        self.lb_custName.setText(_translate("register_2", "真实姓名", None))
        self.pb_openFile.setText(_translate("register_2", "浏览", None))
        self.pb_choiceColor.setText(_translate("register_2", "选择颜色", None))

