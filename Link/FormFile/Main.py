# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'G:\PyProject\FormFile\Main.ui'
#
# Created: Wed May 23 13:10:11 2018
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

class Ui_MainForm(QtGui.QMainWindow):
    def __init__(self):
        super(Ui_MainForm, self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)

    def setupUi(self, MainForm):
        MainForm.setObjectName(_fromUtf8("MainForm"))
        MainForm.resize(383, 629)
        MainForm.setWindowTitle(_fromUtf8(""))
        self.lb_headImg = QtGui.QLabel(MainForm)
        self.lb_headImg.setGeometry(QtCore.QRect(10, 30, 101, 81))
        self.lb_headImg.setObjectName(_fromUtf8("lb_headImg"))
        self.lv_customer = QtGui.QListView(MainForm)
        self.lv_customer.setGeometry(QtCore.QRect(10, 130, 361, 461))
        self.lv_customer.setObjectName(_fromUtf8("lv_customer"))
        self.lb_nick = QtGui.QLabel(MainForm)
        self.lb_nick.setGeometry(QtCore.QRect(140, 30, 54, 12))
        self.lb_nick.setObjectName(_fromUtf8("lb_nick"))

        self.retranslateUi(MainForm)
        QtCore.QMetaObject.connectSlotsByName(MainForm)

    def retranslateUi(self, MainForm):
        MainForm.setWindowTitle(_translate("MainForm", "好友", None))
        self.lb_headImg.setText(_translate("MainForm", "头像", None))
        self.lb_nick.setText(_translate("MainForm", "TextLabel", None))

