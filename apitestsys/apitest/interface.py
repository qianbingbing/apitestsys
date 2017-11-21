# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
import Crud


# 保存项目基础信息
def save_project_base(request):
        p_id = request.POST.get('project-id', "")
        p_name = request.POST.get('project-name', "")
        p_type = request.POST.get('interface-type', "")
        p_desc = request.POST.get('project-desc', "")
        if p_name == '' or p_type == '':
            return JsonResponse({'status': 40001, 'result': '必要参数输入为空'})
        elif len(p_name) >= 20 or len(p_desc) >= 200:
            return JsonResponse({'status': 40002, 'result': '参数输入长度超过最大值'})
        else:
            jsons_data = {}
            jsons_data['name'] = p_name
            jsons_data["interface_type"] = p_type
            jsons_data["desc"] = p_desc
            if Crud.query_json("Project", {"id": p_id}):
                Crud.update("Project", {"id": p_id}, jsons_data)
                return JsonResponse({"status": "ok", "result": "更新数据成功"})
            else:
                jsons_data["id"] = p_id
                Crud.store_json("Project", jsons_data)
                return JsonResponse({"status": "ok", "result": "新增数据成功"})


# 保存邮箱设置
def save_email(request):
                if request.method == "POST":
                    project_id = request.POST.get('project-id', "")
                    switch = request.POST.get('email-switch', "")
                    username = request.POST.get('email-username', "")
                    password = request.POST.get('email-password', "")
                    receiver = request.POST.get('email-receiver', "")
                    cc = request.POST.get('email-cc', "")
                    subject = request.POST.get('email-subject', "")
                    content = request.POST.get('email-content', "")
                    if username == '' or password == '' or receiver == '' or subject == '' or content == '':
                        return JsonResponse({'status': 40001, 'result': '必要参数输入为空'})
                    elif len(username) >= 20 or len(password) >= 20 or len(receiver) >= 100:
                        return JsonResponse({'status': 40002, 'result': '参数输入长度超过最大值'})
                    else:
                        jsons_data = dict(username=username, password=password, sender=username, receiver=receiver,
                                          cc=cc, subject=subject, content=content, project_id=project_id, switch=switch)

                        if Crud.query_json("Email", {"project_id": project_id}):
                            print "更新email数据"
                            Crud.update("Email", {"project_id": project_id}, jsons_data)
                            return JsonResponse({"status": "ok", "result": "更新数据成功"})
                        else:
                            print "插入email数据"
                            Crud.store_json("Email", jsons_data)
                            return JsonResponse({"status": "ok", "result": "新增数据成功"})


# 保存项目环境
def save_env(request):
    p_id = request.POST.get('project-id', "")
    env_name = request.POST.get('env-name', "")
    env_ip = request.POST.get('env-ip', "")
    env_port = request.POST.get('env-port', "")
    if env_name == '' or env_ip == '' or env_port == '':
        return JsonResponse({'status': 40001, 'result': '必要参数输入为空'})
    elif len(env_name) >= 20 or len(env_ip) >= 20 or len(env_port) >= 20:
        return JsonResponse({'status': 40002, 'result': '参数输入长度超过最大值'})
    else:
        jsons_data = dict(name=env_name, ip=env_ip, port=env_port, project_id=p_id)
        Crud.store_json("Environment", jsons_data)
        return JsonResponse({"status": "ok", "result": "新增数据成功"})


# 获取项目列表接口
def get_project_list(request):
    projects = Crud.query_json("Project")
    results = []
    for i in projects:
        # 初始化字典将所有值默认为空
        result = dict.fromkeys(['project_id', 'project_name', 'env_ip', 'db_ip',
                                'email_switch'], "")
        result['project_id'] = i.id
        result['project_name'] = i.name
        envs = Crud.query_json("Environment", {"project_id": i.id, "checked": "1"})
        emails = Crud.query_json("Email", {"project_id": i.id})
        for i in emails:
            result['email_switch'] = i.switch
        for i in envs:
            result['env_ip'] = i.ip
        results.append(result)
    print results
    return JsonResponse({"status": "ok", "result": results})


# 获取项目环境信息接口
def get_envs(request):
    project_id = request.POST.get("project_id")
    if project_id:
        results = []
        envs = Crud.query_json("Environment", {"project_id": project_id})
        for i in envs:
            result = dict(id=i.id, project_id=i.project_id, name=i.name, ip=i.ip, port=i.port, database_ip="")
            database = Crud.query_json("Database", {"project_env_id": i.id})
            for j in database:
                result["database_ip"] = j.ip
            results.append(result)
        return JsonResponse({"status": "ok", "result": results})
    else:
        return JsonResponse({"status": "10001", "result": "参数错误"})


# 获取项目基础信息
def get_project_base(request):
    if request.method == 'POST':
        # 获取项目id
        id = request.POST.get("project_id")
        if id:
            # 获取项目基础信息
            project_base = Crud.query_json("Project", {"id": id})
            results = []
            for i in project_base:
                result = dict(project_name=i.name, interface_type=i.interface_type, project_desc=i.desc)
                results.append(result)
            return JsonResponse({"status": "ok", "result": results})
        else:
            return JsonResponse({"status": "10001", "result": "参数传递错误"})


# 获取database的详细信息
def get_db(request):
    if request.method == "POST":
        # 获取env_id
        env_id = request.POST.get("env_id")
        if env_id:
            databases = Crud.query_json("Database", {"project_env_id": env_id})
            print databases
            results = []
            if databases:
                for i in databases:
                    result = dict(type=i.type, ip=i.ip, port=i.port, username=i.username, password=i.password, name=i.name)
                    results.append(result)

                return JsonResponse({"status": "ok", "result": results})
            else:
                return JsonResponse({"status": "ok", "result": results})


# 保存数据库信息
def save_db(request):
    if request.method == "POST":
        # 获取env_id
        env_id = request.POST.get("env-id")
        type = request.POST.get("db-type")
        ip = request.POST.get("db-ip")
        port = request.POST.get("db-port")
        username = request.POST.get("db-username")
        password = request.POST.get("db-password")
        name = request.POST.get('db-name')
        if env_id:
            databases = Crud.query_json("Database", {"project_env_id": env_id})
            jsons_data = dict(project_env_id=env_id, type=type, ip=ip, port=port,
                              username=username, password=password, name=name)
            if databases:
                Crud.update("Database", {"project_env_id": env_id}, jsons_data)
                return JsonResponse({"status": "ok", "result": "更新数据成功"})
            else:
                Crud.store_json("Database", jsons_data)
                return JsonResponse({"status": "ok", "result": "插入数据成功"})


# 删除环境列表
def delete_env(request):
    if request.method == 'POST':
        env_id = request.POST.get("env_id")
        if env_id:
            try:
                Crud.delete_json("Environment", {"id": env_id})
                Crud.delete_json("Database", {"project_env_id": env_id})
                return JsonResponse({"status": "ok", "result": "删除成功"})
            except:
                return JsonResponse({"status": "10001", "result": "删除失败"})
        else:
            return JsonResponse({"status": "10002", "result": "参数错误"})


# 获取Email信息
def get_email(request):
    if request.method == 'POST':
        # 获取项目id
        project_id = request.POST.get("project_id")
        if project_id:
            # 获取项目基础信息
            emails = Crud.query_json("Email", {"project_id": project_id})
            results = []
            for i in emails:
                result = dict(switch=i.switch, username=i.username, password=i.password, receiver=i.receiver, cc=i.cc,
                              subject=i.subject, content=i.content)
                results.append(result)
            return JsonResponse({"status": "ok", "result": results})
        else:
            return JsonResponse({"status": "10001", "result": "参数传递错误"})


