# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
import logging
from django.shortcuts import render
import models
from django.core import serializers
# Create your views here.
logger = logging.getLogger('django')


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
        else:
            return render(request, 'login.html', {'error': 'username or password error!'})


# 首页
def index(request):
    return render(request, 'index.html')


# 添加项目
def add_project(request):
    id = request.GET.get('id')
    return render(request, "add_project.html", {"id": id})
# 保存项目基础信息
def save_project_base(request):
        p_id = request.POST.get('project-id', "")
        p_name = request.POST.get('project-name', "")
        p_type = request.POST.get('interface-type', "")
        p_desc = request.POST.get('project-desc', "")
        if p_name == '' or p_type == '':
            return JsonResponse({'status': 40001, 'message': '必要参数输入为空'})
        elif len(p_name) >= 20 or len(p_desc) >= 200:
            return JsonResponse({'status': 40002, 'message': '参数输入长度超过最大值'})
        else:
            jsons_data = {}
            jsons_data['name'] = p_name
            jsons_data["interface_type"] = p_type
            jsons_data["desc"] = p_desc
            if query_json("Project", {"id": p_id}):
                update("Project", {"id": p_id}, jsons_data)
                return JsonResponse({"status": "ok", "message": "更新数据成功"})
            else:
                jsons_data["id"] = p_id
                store_json("Project", jsons_data)
                return JsonResponse({"status": "ok", "message": "新增数据成功"})

# 获取项目环境信息接口
def get_envs(request):
    project_id = request.GET.get("project_id")
    if project_id:
        results = []
        envs = query_json("Environment", {"project_id": project_id})
        for i in envs:
            result = {}
            result["id"] = i.id
            result["project_id"] = i.project_id
            result["name"] = i.name
            result["ip"] = i.ip
            result["port"] = i.port
            result["database"] = ""
            database = query_json("Database", {"project_env_id": i.id})
            for j in database:
                result["database"] = j.ip
            results.append(result)
        return JsonResponse({"status": "ok", "result": results})
    else:
        return JsonResponse({"status": "10001", "result": "参数错误"})



def save_env(request):
    p_id = request.POST.get('project-id', "")
    env_name = request.POST.get('env-name', "")
    env_ip = request.POST.get('env-ip', "")
    env_port = request.POST.get('env-port', "")
    if env_name == '' or env_ip == '' or env_port == '':
        return JsonResponse({'status': 40001, 'message': '必要参数输入为空'})
    elif len(env_name) >= 20 or len(env_ip) >= 20 or len(env_port) >=20:
        return JsonResponse({'status': 40002, 'message': '参数输入长度超过最大值'})
    else:
        jsons_data = {}
        jsons_data['name'] = env_name
        jsons_data["ip"] = env_ip
        jsons_data["port"] = env_port
        if query_json("Project", {"id": p_id}):
            update("Project", {"id": p_id}, jsons_data)
            return JsonResponse({"status": "ok", "message": "更新数据成功"})
        else:
            jsons_data["id"] = p_id
            store_json("Project", jsons_data)
            return JsonResponse({"status": "ok", "message": "新增数据成功"})
# 获取项目信息
def get_project(request):
    if request.method == 'GET':
        result = {}
        # 获取项目id
        id = request.GET.get("project_id")
        # 获取项目基础信息
        project_base = query_json("Project", {"id": id})
        result['base'] = project_base
        project_envs = query_json("Environment", {"project_id": id})
        result['envs'] = project_envs
        project_email = query_json("Email", {"project_id": id})
        result['eamil'] = project_email
        return JsonResponse({"status": "ok", "result": result})


# 保存项目环境信息
def save_project_env(request):
    if request.method == 'POST':
        p_id = request.POST.get('project-id', "")


# 保存邮箱设置
def save_email(request):
    return


# 保存测试环境
def save_ev(request):
    return


# 保存数据库设置
def save_db_setting():
    return


# 添加接口
def add_interface(request):
    return render(request, "add_interface.html")


# 项目列表
def project_list(request):
    return render(request, "project_list.html")


# 添加用例
def add_case(request):
    return render(request, "add_testcase.html")


# 接口列表
def interface_list(request):
    return render(request, "interface_list.html")


# 用例列表
def case_list(request):
    return render(request, "testcase_list.html")


# 任务列表
def commission_list(request):
    return render(request, "commisson_list.html")


# 报告列表
def report_list(request):
    return render(request, "report_list.html")


# 报告详情
def report_detail(request):
    return render(request, "report_detail.html")

##################################################################
#                   PUBLIC METHODS CRUD                          #
##################################################################


def store_json(tablename, jsondata):
    """
    Store json data into DB
    @parameter declaration
    tablename: the table to insert
    jsondata:  json data like {}

    """
    table = getattr(models, tablename)
    table.objects.create(**jsondata)


def delete_json(tablename, filter=None):
    """
    Delete all data or qualified data
    @parameter declaration
    tablename: the table you want delete
    filter:  Filter condition use dict type to define the context
    """
    table = getattr(models, tablename)
    if filter:
        table.objects.filter(**filter).delete()
    else:
        table.objects.filter().delete()


def query_json(tablename,filter):
    """
    Returns all data or qualified data
    @parameter declaration
    tablename: The table name
    filter: Filter condition use dict type to define the context

    """
    table = getattr(models, tablename)
    querySet = table.objects.filter(**filter)
    print querySet
    return querySet

def update(tablename, filter, context):
    """
    update qualified data
    @parameter declaration
    tablename: The table name
    filter: Filter condition use dict type to define the context
    context: The json data data
    """
    table = getattr(models, tablename)
    table.objects.filter(**filter).update(**context)


