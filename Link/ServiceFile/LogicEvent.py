# -*- coding: utf-8 -*-
import sys
sys.path.append('../CommanFile')
reload(sys);
sys.setdefaultencoding('utf8');
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
        self.logon.lb_headImg.setPixmap(png)

    def getAllCustom(self,account):
        self.main.lb_nick.setText(account)
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
                headImg = row['HeadImg']
        png = QtGui.QPixmap(headImg)
        self.main.lb_headImg.setPixmap(png)
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
        accountInfoData={
            "Account":str(self.register.le_accountName.text()),
            "Pwd":str(self.register.le_pwd.text()),
            "HeadImg":str(self.register.le_headImg.text()).replace('\',''\\'),
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

