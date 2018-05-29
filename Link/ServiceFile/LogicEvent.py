# -*- coding: utf-8 -*-
import sys
sys.path.append('../CommanFile')
import time;
from MySQLHelper import MySQLHelper
from PyQt4 import QtCore, QtGui

sqlHelper = MySQLHelper("localhost", "root", "123456")
sqlHelper.setDB("link")

class logonEvent:
    def __init__(self,logon,main):
        self.logon = logon
        self.main = main

    def loggon(self):
        account = unicode(self.logon.le_account.text().toUtf8(),'utf-8','ignore').encode('utf-8')
        pwd = unicode(self.logon.le_pwd.text().toUtf8(),'utf-8','ignore').encode('utf-8')
        sql="select count(*) from accountInfo where Account='{0}' and Pwd = '{1}'".format(account,pwd)
        count = sqlHelper.queryOnlyRow(sql).values()[0]
        if count>0:
            self.logon.close()
            self.main.show()
            self.getAllCustom(account)

    def getHeadImg(self):
        account = unicode(self.logon.le_account.text().toUtf8(),'utf-8','ignore').encode('utf-8')
        sql = "select HeadImg from accountInfo where Account like '%{0}%'".format(account)
        imgStr = sqlHelper.queryOnlyRow(sql).values()[0]
        png = QtGui.QPixmap(imgStr)
        self.logon.lb_headImg.setScaledContents(True)
        self.logon.lb_headImg.setPixmap(png)

    def getAllCustom(self,account):
        sql = "select NickName,Account,CustName,Address,Mobile,FontColorId,Sex,HeadImg \
               from customer as cust \
               inner join accountInfo as info \
               on cust.AcctountInfoId = info.Id"
        data = sqlHelper.queryAll(sql)
        model = QtGui.QStandardItemModel(self.main.lv_customer)
        for row in data:
            if row['Account'] == account:
                nickName = row['NickName']
                headImg = row['HeadImg']
            else:
                item = QtGui.QStandardItem(row['NickName'].decode('utf8'))
                icon_expand = QtGui.QIcon(row['HeadImg'])
                item.setIcon(icon_expand)
                model.appendRow(item)
        png = QtGui.QPixmap(headImg)
        self.main.lb_headImg.setScaledContents(True)
        self.main.lb_headImg.setPixmap(png)
        self.main.lb_nick.setText(nickName.decode('utf8'))
        self.main.lv_customer.setModel(model)


class registerEvent:
    def __init__(self,register):
        self.register = register

    def reg(self):
        fontColorData={
            "ColorCode":unicode(self.register.le_fontColor.text().toUtf8(),'utf-8','ignore').encode('utf-8'),
            "Des":""
        }
        sqlHelper.insert("fontColor",fontColorData)
        colorId = sqlHelper.getLastInsertRowId()
        headImg = unicode(self.register.le_headImg.text().toUtf8(),'utf-8','ignore').encode('utf-8').replace('\\', '\\\\')
        accountInfoData={
            "Account":unicode(self.register.le_accountName.text().toUtf8(),'utf-8','ignore').encode('utf-8'),
            "Pwd":unicode(self.register.le_pwd.text().toUtf8(),'utf-8','ignore').encode('utf-8'),
            "HeadImg":headImg,
            "FontColorId":colorId,
        }
        sqlHelper.insert("accountInfo",accountInfoData)
        accountInfoId = sqlHelper.getLastInsertRowId()
        sex = 1 if unicode(self.register.le_sex.text().toUtf8(),'utf-8','ignore').encode('utf-8').strip()=="男" else 0
        customerData={
            "CustName":unicode(self.register.le_custName.text().toUtf8(),'utf-8','ignore').encode('utf-8'),
            "Sex":sex,
            "NickName":unicode(self.register.le_nickName.text().toUtf8(),'utf-8','ignore').encode('utf-8'),
            "Address":unicode(self.register.le_address.text().toUtf8(),'utf-8','ignore').encode('utf-8'),
            "Mobile":unicode(self.register.le_phone.text().toUtf8(),'utf-8','ignore').encode('utf-8'),
            "AcctountInfoId":accountInfoId
        }
        sqlHelper.insert("customer", customerData)

class mainEvent:
    def __init__(self,main,message):
        self.main = main
        self.message = message

    def openMessage(self,index):
        target_nickName = unicode(index.data().toString().toUtf8(),'utf-8','ignore').encode('utf-8')
        sql = "select NickName,Account,CustName,Address,Mobile,FontColorId,Sex,HeadImg \
               from customer as cust \
               inner join accountinfo as info \
               on cust.AcctountInfoId = info.Id where NickName = '{0}'".format(target_nickName)
        model = sqlHelper.queryOnlyRow(sql)
        self.message.lb_sex.setText(u"性别:男" if model['Sex'] == 1 else u"性别:女")
        self.message.lb_nickName.setText(model['NickName'].decode('utf8'))
        png = QtGui.QPixmap(model['HeadImg'])
        self.message.lb_headImg.setScaledContents(True)
        self.message.lb_headImg.setPixmap(png)
        currentLoggon_nickName = unicode(self.main.lb_nick.text().toUtf8(),'utf-8','ignore').encode('utf-8')
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
            sql = "select * from AccountInfo where Id = {0}".format(sendAccount)
            sendData = sqlHelper.queryOnlyRow(sql)
            icon_expand = QtGui.QIcon(sendData['HeadImg'])
            item.setIcon(icon_expand)
            itemModel.appendRow(item)
        self.message.lv_message.setModel(itemModel)

class messageEvent:
    def __init__(self,message,main):
        self.message = message
        self.main = main

    def sendMessage(self):
        currentNick = unicode(self.main.lb_nick.text().toUtf8(),'utf-8','ignore').encode('utf-8')
        targetNick = unicode(self.message.lb_nickName.text().toUtf8(),'utf-8','ignore').encode('utf-8')
        sql = "select AcctountInfoId from Customer where NickName= '{0}'"
        currentAccountId = sqlHelper.queryOnlyRow(sql.format(currentNick))["AcctountInfoId"]
        targetAccountId = sqlHelper.queryOnlyRow(sql.format(targetNick))["AcctountInfoId"]
        messageContent = unicode(self.message.te_talk.toPlainText().toUtf8(),'utf-8','ignore').encode('utf-8')
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

