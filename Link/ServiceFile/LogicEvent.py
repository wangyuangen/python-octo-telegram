# -*- coding: utf-8 -*-
import sys
sys.path.append('../CommanFile')
from MySQLHelper import MySQLHelper
from PyQt4 import QtCore, QtGui

sqlHelper = MySQLHelper("localhost", "root", "123456")
sqlHelper.setDB("link")

class logonEvent:
    def __init__(self,logon,main):
        self.logon = logon
        self.main = main

    def loggon(self):
        account = str(self.logon.le_account.text())
        pwd = str(self.logon.le_pwd.text())
        sql="select count(*) from accountInfo where Account='{0}' and Pwd = '{1}'".format(account,pwd)
        count = sqlHelper.queryOnlyRow(sql).values()[0]
        if count>0:
            self.logon.close()
            self.main.show()
            self.getAllCustom(account)

    def getHeadImg(self):
        account = str(self.logon.le_account.text())
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
            item = QtGui.QStandardItem(row['NickName'])
            icon_expand = QtGui.QIcon(row['HeadImg'])
            item.setIcon(icon_expand)
            model.appendRow(item)
            if row['Account'] == account:
                nickName = row['NickName']
                headImg = row['HeadImg']
        png = QtGui.QPixmap(headImg)
        self.main.lb_headImg.setScaledContents(True)
        self.main.lb_headImg.setPixmap(png)
        self.main.lb_nick.setText(nickName)
        self.main.lv_customer.setModel(model)


class registerEvent:
    def __init__(self,register):
        self.register = register

    def reg(self):
        fontColorData={
            "ColorCode":str(self.register.le_fontColor.text()),
            "Des":""
        }
        sqlHelper.insert("fontColor",fontColorData)
        colorId = sqlHelper.getLastInsertRowId()
        headImg = str(self.register.le_headImg.text()).replace('\\', '\\\\')
        accountInfoData={
            "Account":str(self.register.le_accountName.text()),
            "Pwd":str(self.register.le_pwd.text()),
            "HeadImg":headImg,
            "FontColorId":colorId,
        }
        sqlHelper.insert("accountInfo",accountInfoData)
        accountInfoId = sqlHelper.getLastInsertRowId()
        sex = 1 if str(self.register.le_sex.text()).strip()=="男" else 0
        customerData={
            "CustName":str(self.register.le_accountName.text()),
            "Sex":sex,
            "NickName":str(self.register.le_nickName.text()),
            "Address":str(self.register.le_address.text()),
            "Mobile":str(self.register.le_phone.text()),
            "AcctountInfoId":accountInfoId
        }
        sqlHelper.insert("customer", customerData)

class mainEvent:
    def __init__(self,main,message):
        self.main = main
        self.message = message

    def openMessage(self,index):
        #model = QtGui.QStandardItemModel(self.main.lv_customer)
        #q = index.row()
        target_nickName = str(index.data().toString()).strip()
        sql = "select NickName,Account,CustName,Address,Mobile,FontColorId,Sex,HeadImg \
               from customer as cust \
               inner join accountinfo as info \
               on cust.AcctountInfoId = info.Id where NickName = '{0}'".format(target_nickName)
        model = sqlHelper.queryOnlyRow(sql)
        self.message.lb_sex.setText(u"性别:男" if model['Sex'] == 1 else u"性别:女")
        self.message.lb_nickName.setText(model['NickName'])
        png = QtGui.QPixmap(model['HeadImg'])
        self.message.lb_headImg.setScaledContents(True)
        self.message.lb_headImg.setPixmap(png)
        currentLoggon_nickName = str(self.main.lb_nick.text())
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
            item = QtGui.QStandardItem(row['Message'])
            sendAccount = row['SendAccount']
            sql = "select * from AccountInfo where Id = {0}".format(sendAccount)
            sendData = sqlHelper.queryOnlyRow(sql)
            icon_expand = QtGui.QIcon(sendData['HeadImg'])
            item.setIcon(icon_expand)
            itemModel.appendRow(item)
        self.message.lv_message.setModel(itemModel)