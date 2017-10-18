"""apitestsys URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URL conf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from apitest import views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^register/', views.register),
    url(r'^login/', views.login),
    url(r'^login_action/', views.login_action),
    url(r'^index/', views.index),
    url(r'^addProject/', views.add_project),
    url(r'^projectList/', views.project_list),
    url(r'^addInterface/', views.add_interface),
    url(r'^addCase/', views.add_case),
    url(r'^interfaceList/', views.interface_list),
    url(r'^caseList/', views.case_list),
    url(r'^commissionList/', views.commission_list),
    url(r'^reportList/', views.report_list),
    url(r'^reportDetail/', views.report_detail),
    url(r'^save_project_base/', views.save_project_base),
    url(r'^get_project/', views.get_project),
    url(r'^get_envs/', views.get_envs),
    url(r'^save_env/', views.save_env),
    url(r'^save_email/', views.save_email),
]
