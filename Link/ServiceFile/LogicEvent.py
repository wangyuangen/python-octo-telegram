 # -*- coding: utf-8 -*-
import sys
sys.path.append('../CommanFile')
import time
from MySQLHelper import MySQLHelper
from PyQt4 import QtCore, QtGui
import ConfigParser

config = ConfigParser.ConfigParser()
config.read('../CommanFile/config.ini')
server = config.get('db','server')
account = config.get('db','account')
password = config.get('db','password')
dbName = config.get('db','dbname')
sqlHelper = MySQLHelper(server, account, password)
sqlHelper.setDB(dbName)

def strParse(object):
    return unicode(object.toUtf8(),'utf-8','ignore').encode('utf-8')

class logonEvent:
    def __init__(self,logon,main):
        self.logon = logon
        self.main = main

    def loggon(self):
        account = strParse(self.logon.le_account.text())
        pwd = strParse(self.logon.le_pwd.text())
        sql="select count(*) from accountinfo where Account='{0}' and Pwd = '{1}'".format(account,pwd)
        count = sqlHelper.queryOnlyRow(sql).values()[0]
        if count>0:
            self.logon.close()
            self.main.show()
            self.getAllCustom(account)
        else:
            QtGui.QMessageBox.information(self.logon, u'提示信息', u'登录失败,用户名或密码不存在!')

    def getHeadImg(self):
        account = strParse(self.logon.le_account.text())
        sql = "select HeadImg from accountinfo where Account like '%{0}%'".format(account)
        imgStr = sqlHelper.queryOnlyRow(sql).values()[0]
        photo = QtGui.QPixmap()
        photo.loadFromData(QtCore.QByteArray(imgStr),'jpg')
        self.logon.lb_headImg.setScaledContents(True)
        self.logon.lb_headImg.setPixmap(photo)

    def getAllCustom(self,account):
        sql = "select NickName,Account,CustName,Address,Mobile,FontColorId,Sex,HeadImg \
               from customer as cust \
               inner join accountinfo as info \
               on cust.AcctountInfoId = info.Id"
        data = sqlHelper.queryAll(sql)
        model = QtGui.QStandardItemModel(self.main.lv_customer)
        for row in data:
            if row['Account'] == account:
                nickName = row['NickName']
                headImg = row['HeadImg']
            else:
                item = QtGui.QStandardItem(row['NickName'].decode('utf8'))
                img = open('head.jpb','wb')
                img.write(row['HeadImg'])
                img.close()
                icon_expand = QtGui.QIcon(img.name)
                item.setIcon(icon_expand)
                item.setBackground(QtGui.QBrush(QtCore.Qt.lightGray))
                model.appendRow(item)
        photo = QtGui.QPixmap()
        photo.loadFromData(QtCore.QByteArray(headImg), 'jpg')
        self.main.lb_headImg.setScaledContents(True)
        self.main.lb_headImg.setPixmap(photo)
        self.main.lb_nick.setText(nickName.decode('utf8'))
        self.main.lv_customer.setModel(model)


class registerEvent:
    def __init__(self,register):
        self.register = register

    def reg(self):
        fontColorData={
            "ColorCode":strParse(self.register.le_fontColor.text()),
            "Des":""
        }
        sqlHelper.insert("fontcolor",fontColorData)
        colorId = sqlHelper.getLastInsertRowId()
        headImg = sqlHelper.getImgStr(strParse(self.register.le_headImg.text()))
        accountInfoData={
            "Account":strParse(self.register.le_accountName.text()),
            "Pwd":strParse(self.register.le_pwd.text()),
            "HeadImg":headImg,
            "FontColorId":colorId,
        }
        sqlHelper.insert("accountinfo",accountInfoData)
        accountInfoId = sqlHelper.getLastInsertRowId()
        sex = 1 if strParse(self.register.le_sex.text()).strip()=="男" else 0
        customerData={
            "CustName":strParse(self.register.le_custName.text()),
            "Sex":sex,
            "NickName":strParse(self.register.le_nickName.text()),
            "Address":strParse(self.register.le_address.text()),
            "Mobile":strParse(self.register.le_phone.text()),
            "AcctountInfoId":accountInfoId
        }
        sqlHelper.insert("customer", customerData)
        QtGui.QMessageBox.information(self.register,u'提示信息',u'用户信息注册成功')

    def openFile(self):
        fname = QtGui.QFileDialog.getOpenFileName(self.register, '打开文件','./',("Images (*.png *.xpm *.jpg)"))
        if fname:
            self.register.le_headImg.setText(fname)

    def choiceColor(self):
        col = QtGui.QColorDialog.getColor()
        if col.isValid():
            self.register.le_fontColor.setText(col.name())

class mainEvent:
    def __init__(self,main,message):
        self.main = main
        self.message = message

    def openMessage(self,index):
        target_nickName = strParse(index.data().toString())
        sql = "select NickName,Account,CustName,Address,Mobile,FontColorId,Sex,HeadImg \
               from customer as cust \
               inner join accountinfo as info \
               on cust.AcctountInfoId = info.Id where NickName = '{0}'".format(target_nickName)
        model = sqlHelper.queryOnlyRow(sql)
        self.message.lb_sex.setText(u"性别:男" if model['Sex'] == 1 else u"性别:女")
        self.message.lb_nickName.setText(model['NickName'].decode('utf8'))
        photo = QtGui.QPixmap()
        photo.loadFromData(QtCore.QByteArray(model['HeadImg']), 'jpg')
        self.message.lb_headImg.setScaledContents(True)
        self.message.lb_headImg.setPixmap(photo)
        currentLoggon_nickName = strParse(self.main.lb_nick.text())
        self.showMessageBox(target_nickName,currentLoggon_nickName)
        self.message.show()

    def showMessageBox(self,target_nickName,currentLoggon_nickName):
        sql = "select * from message where SendAccount in  \
                      (select AcctountInfoId from customer where NickName = '{0}' or NickName = '{1}')\
                       and TargetAccount in  \
                      (select AcctountInfoId from customer where NickName = '{0}' or NickName = '{1}')".format(
            target_nickName, currentLoggon_nickName)
        data = sqlHelper.queryAll(sql)
        itemModel = QtGui.QStandardItemModel(self.main.lv_customer)
        for row in data:
            item = QtGui.QStandardItem(row['Message'].decode('utf8'))
            sendAccount = row['SendAccount']
            sql = "select Account,Pwd,HeadImg,ColorCode from accountinfo as info \
                   left join fontcolor as color \
                   on info.fontColorId = color.Id where info.Id ={0}".format(sendAccount)
            sendData = sqlHelper.queryOnlyRow(sql)
            img = open('head.img','wb')
            img.write(sendData['HeadImg'])
            img.close()
            icon_expand = QtGui.QIcon(img.name)
            item.setIcon(icon_expand)
            itemModel.appendRow(item)
        self.message.lv_message.setModel(itemModel)

class messageEvent:
    def __init__(self,message,main):
        self.message = message
        self.main = main

    def sendMessage(self):
        currentNick = strParse(self.main.lb_nick.text())
        targetNick = strParse(self.message.lb_nickName.text())
        sql = "select AcctountInfoId from customer where NickName= '{0}'"
        currentAccountId = sqlHelper.queryOnlyRow(sql.format(currentNick))["AcctountInfoId"]
        targetAccountId = sqlHelper.queryOnlyRow(sql.format(targetNick))["AcctountInfoId"]
        messageContent = strParse(self.message.te_talk.toPlainText())
        data ={
            "SendAccount":currentAccountId,
            "TargetAccount":targetAccountId,
            "Message":messageContent,
            "SendTime":time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        }
        sqlHelper.insert("message",data)
        self.message.te_talk.setHtml("")
        main = mainEvent(self.main,self.message);
        main.showMessageBox(targetNick,currentNick);

