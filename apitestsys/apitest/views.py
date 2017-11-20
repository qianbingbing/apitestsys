# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
import logging
from django.shortcuts import render
import models
import json
from django.core import serializers
# Create your views here.


# 注册页面
def register(request):
    return render(request, 'register.html')


# 登录页面
def login(request):
    return render(request, "login.html")


# 账号登录
def login_action(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
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
        else:
            return render(request, 'login.html', {'error': 'username or password error!'})


# 首页
def index(request):
    return render(request, 'index.html')


# 添加项目页面
def add_project(request):
    id = request.GET.get('id')
    return render(request, "add_project.html", {"id": id})





# 保存数据库设置
def save_db_setting():

    return


# 添加接口页面
def add_interface(request):
    return render(request, "add_interface.html")


# 项目列表页面
def project_list(request):
    return render(request, "project_list.html")


# 添加用例页面
def add_case(request):
    return render(request, "add_testcase.html")


# 接口列表页面
def interface_list(request):
    return render(request, "interface_list.html")


# 用例列表页面
def case_list(request):
    return render(request, "testcase_list.html")


# 任务列表页面
def commission_list(request):
    return render(request, "commisson_list.html")


# 报告列表页面
def report_list(request):
    return render(request, "report_list.html")


# 报告详情页面
def report_detail(request):
    return render(request, "report_detail.html")




