# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
import logging
from django.shortcuts import render
import time
# Create your views here.
logger = logging.getLogger('django')
#注册页面
def register(request):
    return render(request, 'register.html')
#登录页面
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
#首页
def index(request):
    return render(request, 'index.html')
#添加项目
def addProject(requst):
    return render(requst, "add_project.html")
#保存项目信息
def saveProject(request):
    if request.method == 'POST':
        name = request.POST.get('project-name', "")
        type = request.POST.get('interface-type', "")
        desc = request.POST.get('project-desc', "")
        if name == '' or type == '' :
            return JsonResponse({'status': 40001, 'message': 'some paramters is null'})
        elif len(name)>=20 or len(desc)>=200:
            return JsonResponse({'status': 40002, 'message': 'some paramters is null'})
        else:
            jsons_data = {}
            jsons_data["id"] = int(time.time())
            jsons_data["name"] = name
            jsons_data["desc"] = desc
            #jsons_data["leader"] = leader
            #jsons_data["remark"] = notes
            #store_json("Project", jsons_data)
            return HttpResponseRedirect('/index')

#保存邮箱设置
def saveEmail(request):
    return
#保存测试环境
def saveEv(request):
    return
# 保存数据库设置
def saveDBsetting():
    return

#添加接口
def addInterface(request):
    return render(request, "add_interface.html")
#项目列表
def projectList(request):
    return render(request, "project_list.html")
#添加用例
def addTestcase(request):
    return render(request, "add_testcase.html")
#接口列表
def interfaceList(request):
    return render(request, "interface_list.html")
#用例列表
def testcaseList(request):
    return render(request, "testcase_list.html")
#任务列表
def commissonList(request):
    return render(request, "commisson_list.html")
#报告列表
def reportList(request):
    return render(request, "report_list.html")
#报告详情
def reportDetail(request):
    return render(request, "report_detail.html")
