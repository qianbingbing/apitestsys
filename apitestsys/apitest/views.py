# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse,HttpResponseRedirect
import logging
from django.shortcuts import render
# Create your views here.
logger = logging.getLogger('django')
#注册
def register(request):
    return render(request, 'register.html')
# 登录页面
def login(request):
    return render(request, "login.html")
#账号登录
def login_action(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        logger.info(username)
        logger.info(password)
        '''
        user = authenticate(username=username, password=password)
        if user is not None:
            login(user)
            response = HttpResponseRedirect('index/')
            return response
        '''
        if username == "admin" and password == "admin":
            response = HttpResponseRedirect('/index/')
            return response
            logger.info("登录成功")
        else:
            return render(request, 'login.html', {'error': 'username or password error!'})
            logger.error("登录成功")
# 首页
def index(request):
    return render(request, 'index.html')
#添加项目
def addProject(requst):
    
    return render(requst, "add_project.html")
def addInterface(request):
    return render(request, "add_interface.html")
#添加接口
def projectList(request):
    return render(request, "project_list.html")
#添加用例
def addTestcase(request):
    return render(request, "add_testcase.html")
def interfaceList(request):
    return render(request, "interface_list.html")
def testcaseList(request):
    return render(request, "testcase_list.html")
def commissonList(request):
    return render(request, "commisson_list.html")
def reportList(request):
    return render(request, "report_list.html")
def reportDetail(request):
    return render(request, "report_detail.html")
