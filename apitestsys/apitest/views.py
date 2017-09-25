# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
import logging
from django.shortcuts import render
import models

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
        else:
            return render(request, 'login.html', {'error': 'username or password error!'})

#首页
def index(request):
    return render(request, 'index.html')
#添加项目
def addProject(request):
    id = request.GET.get('id')
    return render(request, "add_project.html", {"id":id})
#保存项目信息

def ajax_dict(request):
        p_id = request.POST.get('project-id', "")
        p_name = request.POST.get('project-name', "")
        p_type = request.POST.get('interface-type', "")
        p_desc = request.POST.get('project-desc', "")
        if p_name == '' or p_type == '':
            return JsonResponse({'status': 40001, 'message': '姓名或类型参数输入为空'})
        elif len(p_name) >= 20 or len(p_desc) >= 200:
            return JsonResponse({'status': 40002, 'message': '参数输入长度超过最大值'})
        else:
            jsons_data = {}
            jsons_data['name'] = p_name
            jsons_data["interface_type"] = p_type
            jsons_data["desc"] = p_desc
            print query_json("Project", {"id": p_id})
            if query_json("Project",{"id": p_id}):
                update("Project", {"id": p_id}, jsons_data)
                return JsonResponse({"status": "ok", "message": "更新数据成功"})
            else:
                jsons_data["id"] = p_id
                print jsons_data
                print "列表为空，进行新增操作"
                store_json("Project", jsons_data)
                return JsonResponse({"status": "ok", "message": "新增数据成功"})
def save_base(request):
    if request.method == 'POST':
        p_id = request.POST.get('project-id', "")
        p_name = request.POST.get('project-name', "")
        p_type = request.POST.get('interface-type', "")
        p_desc = request.POST.get('project-desc', "")
        if p_name == '' or p_type == '':
            return JsonResponse({'status': 40001, 'message': '姓名或类型参数输入为空'})
        elif len(p_name) >= 20 or len(p_desc) >= 200:
            return JsonResponse({'status': 40002, 'message': '参数输入长度超过最大值'})
        else:
            jsons_data = {}
            jsons_data["id"] = p_id
            jsons_data['name'] = p_name
            jsons_data["interface_type"] = p_type
            jsons_data["desc"] = p_desc
            if query_json("Project", {"id": id}):
                print "列表不为空，进行更新操作"
                update("Project", {"id": id}, jsons_data)
                return JsonResponse({"status": "ok", "message": "更新数据成功"})
            else:
                print "列表为空，进行新增操作"
                store_json("Project", jsons_data)
                return JsonResponse({"status": "ok", "message": "新增数据成功"})
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


##################################################################
# PUBLIC METHODS THAT ALTER ATTRIBUTES AND RETURN A NEW QUERYSET #
##################################################################
"""
Store json data into DB
@parameter declaration
tablename: the table to insert
jsondata:  json data like {}
"""
def store_json(tablename, jsondata):
    table = getattr(models, tablename)
    table.objects.create(**jsondata)

"""
Delete all data or qualified data
@parameter declaration
tablename: the table you want delete
filter:  Filter condition use dict type to define the context 
"""
def delete_json(tablename,filter=None):
    table = getattr(models, tablename)
    if filter == None:
        table.objects.filter().delete()
    else:
        table.objects.filter(**filter).delete()
"""
Returns all data or qualified data
@parameter declaration
tablename: The table name
filter: Filter condition use dict type to define the context 
"""
def query_json(tablename,filter1):
    table = getattr(models, tablename)
    return table.objects.filter(**filter1)

"""
update qualified data
@parameter declaration
tablename: The table name
filter: Filter condition use dict type to define the context 
context: The json data data 
"""
def update(tablename,filter,context):
    table = getattr(models, tablename)
    table.objects.filter(**filter).update(**context)
