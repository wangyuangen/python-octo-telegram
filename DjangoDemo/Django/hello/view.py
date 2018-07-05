#--encoding:utf-8-- #

from django.http import HttpResponse
from django.shortcuts import render
from MySQLHelper import MySQLHelper

def main(request):
    return render(request,'main.html')

def login_form(request):
    context ={}
    context['infomation']="Don't have an account?   Sign up"
    return render(request,'login.html',context)

def login(request):
    context={}
    request.encoding = 'utf-8'
    sqlHelper = MySQLHelper('47.75.63.12','root','root')
    sqlHelper.setDB('link')
    account = request.GET['account']
    pwd =request.GET['passWord']
    sql = "select count(*) from accountinfo where Account='{0}' and Pwd = '{1}'".format(account, pwd)
    count = sqlHelper.queryOnlyRow(sql).values()[0]
    if count > 0:
        return render(request,'main.html',context)
    else:
        context['infomation'] = u"账号或密码错误,登陆失败"
        return render(request, 'login.html', context)
