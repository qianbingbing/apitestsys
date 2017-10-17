# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
# Create your models here.


# 项目设置-测试环境
class Environment(models.Model):
    name = models.CharField(max_length=20,null=True)
    ip = models.CharField(max_length=20, null=True)
    port = models.CharField(max_length=40, null=True)
    checked = models.BooleanField()
    project_id = models.CharField(max_length=100, null=True)
    data_base_id = models.CharField(max_length=200, null=True)


# 项目设置-数据库
class Database(models.Model):
    project_env_id = models.IntegerField(null=True)
    type = models.CharField(max_length=20, null=True)
    ip = models.CharField(max_length=20, null=True)
    port = models.CharField(max_length=40, null=True)
    username = models.CharField(max_length=40, null=True)
    password = models.CharField(max_length=40, null=True)
    name = models.CharField(max_length=40, null=True)


# 项目设置-基础信息
class Project(models.Model):
    # 项目id
    id = models.CharField(max_length=32, primary_key=True)
    # 项目名称
    name = models.CharField(max_length=20, null=True)
    # 项目描述
    desc = models.CharField(max_length=40, null=True)
    # 项目接口类型
    interface_type = models.CharField(max_length=100, null=True)


# 项目设置-邮箱设置
class Email(models.Model):
    # 项目id
    project_id = models.CharField(max_length=32, primary_key=True)
    # 开关
    switch = models.BooleanField()
    # 用户名
    user_name = models.CharField(max_length=20, null=True)
    # 密码
    password = models.CharField(max_length=40, null=True)
    # 发件人
    sender = models.CharField(max_length=20, null=True)
    # 主送人
    receiver = models.CharField(max_length=100, null=True)
    # 抄送人
    cc = models.CharField(max_length=100, null=True)
    # 邮件主题
    subject = models.CharField(max_length=100, null=True)
    # 邮件内容
    context = models.CharField(max_length=1000, null=True)


# 接口
class Interface(models.Model):
    # 项目id
    project_id = models.IntegerField()
    # 接口名称
    name = models.CharField(max_length=20)
    # 请求路径
    url = models.CharField(max_length=20)
    # 请求方式
    type = models.CharField(max_length=10)
    # 结果类型
    result_type = models.CharField(max_length=10)
    # HEADERS
    headers = models.CharField(max_length=100)
    # 请求数据
    request = models.CharField(max_length=100, null=True)
    # 返回结果
    response = models.CharField(max_length=100)


# 测试任务
class Commission(models.Model):
    # 任务编号
    identifier = models.IntegerField()
    # 创建时间
    crate_time = models.CharField(max_length=20)
    # 任务状态
    status = models.CharField(max_length=20)
    # 任务状态
    type= models.CharField(max_length=10)
    # 执行者
    executor = models.CharField(max_length=10)
    # 项目
    projects = models.CharField(max_length=50)
    # 测试结果
    test_result = models.CharField(max_length=10)


# 测试用例-基础信息
class Testcase(models.Model):
    # 项目名称
    project_name = models.CharField(max_length=30)
    # 接口名称
    interface_name = models.CharField(max_length=20)
    # 用例编号
    case_number = models.IntegerField()
    # 用例序号
    case_index = models.IntegerField()


# 测试用例-预置操作
class Tpreoperation(models.Model):
    # 接口名称
    interface_name = models.CharField(max_length=10)
    # 用例名称
    case_name = models.CharField(max_length=20)
    # 关联用例基础信息
    basic = models.ForeignKey('Testcase')


# 测试用例-据库变量
class Tdatavar(models.Model):
    # 名称
    name = models.CharField(max_length=10)
    # 变量名
    var_name = models.CharField(max_length=10)
    # sql语句
    sql = models.CharField(max_length=10)
    # 自定义变量名
    custom_name = models.CharField(max_length=10)
    # 关联用例基础信息
    basic = models.ForeignKey('Testcase')


# 测试用例-请求数据
class Trequest(models.Model):
    # 请求key
    request_key = models.CharField(max_length=20)
    # 请求value
    request_value = models.CharField(max_length=20)
    # 关联用例基础信息
    basic = models.ForeignKey('Testcase')


# 测试用例-检查返回结果
class Tresponse(models.Model):
    # 返回结果key
    response_key = models.CharField(max_length=20)
    # 返回结果value
    response_value = models.CharField(max_length=20)
    # 关联用例基础信息
    basic = models.ForeignKey('Testcase')


# 测试用例-检查数据库
class Tcheckdb(models.Model):
    # 检查点名称
    name = models.CharField(max_length=20)
    # sql语句
    sql = models.CharField(max_length=100)
    # 预期结果
    expectation = models.CharField(max_length=50)
    # 关联用例基础信息
    basic = models.ForeignKey('Testcase')


