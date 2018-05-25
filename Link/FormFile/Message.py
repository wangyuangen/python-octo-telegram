# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\WorkSpace\����\Project\python-octo-telegram\Link\FormFile\Message.ui'
#
# Created: Fri May 25 17:42:47 2018
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

class Ui_message(QtGui.QMainWindow):
    def __init__(self):
        super(Ui_message, self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)

    def setupUi(self, message):
        message.setObjectName(_fromUtf8("message"))
        message.resize(518, 508)
        self.verticalScrollBar = QtGui.QScrollBar(message)
        self.verticalScrollBar.setGeometry(QtCore.QRect(490, 70, 16, 241))
        self.verticalScrollBar.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar.setObjectName(_fromUtf8("verticalScrollBar"))
        self.te_talk = QtGui.QTextEdit(message)
        self.te_talk.setGeometry(QtCore.QRect(10, 340, 481, 111))
        self.te_talk.setObjectName(_fromUtf8("te_talk"))
        self.pb_send = QtGui.QPushButton(message)
        self.pb_send.setGeometry(QtCore.QRect(340, 470, 75, 23))
        self.pb_send.setObjectName(_fromUtf8("pb_send"))
        self.pb_cancel = QtGui.QPushButton(message)
        self.pb_cancel.setGeometry(QtCore.QRect(420, 470, 75, 23))
        self.pb_cancel.setObjectName(_fromUtf8("pb_cancel"))
        self.lb_headImg = QtGui.QLabel(message)
        self.lb_headImg.setGeometry(QtCore.QRect(10, 10, 54, 51))
        self.lb_headImg.setObjectName(_fromUtf8("lb_headImg"))
        self.lb_nickName = QtGui.QLabel(message)
        self.lb_nickName.setGeometry(QtCore.QRect(80, 20, 54, 12))
        self.lb_nickName.setObjectName(_fromUtf8("lb_nickName"))
        self.lb_sex = QtGui.QLabel(message)
        self.lb_sex.setGeometry(QtCore.QRect(80, 50, 54, 12))
        self.lb_sex.setObjectName(_fromUtf8("lb_sex"))
        self.lv_message = QtGui.QListView(message)
        self.lv_message.setGeometry(QtCore.QRect(10, 70, 481, 241))
        self.lv_message.setObjectName(_fromUtf8("lv_message"))

        self.retranslateUi(message)
        QtCore.QMetaObject.connectSlotsByName(message)

    def retranslateUi(self, message):
        message.setWindowTitle(_translate("message", "Message", None))
        self.pb_send.setText(_translate("message", "发送", None))
        self.pb_cancel.setText(_translate("message", "关闭", None))
        self.lb_headImg.setText(_translate("message", "TextLabel", None))
        self.lb_nickName.setText(_translate("message", "TextLabel", None))
        self.lb_sex.setText(_translate("message", "TextLabel", None))

