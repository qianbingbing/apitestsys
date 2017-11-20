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
from apitest import interface
urlpatterns = [
    # page url list
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
    #  interface url list
    url(r'^save_project_base/', interface.save_project_base),
    url(r'^get_project/', interface.get_project_base),
    url(r'^get_envs/', interface.get_envs),
    url(r'^save_env/', interface.save_env),
    url(r'^save_email/', interface.save_email),
    url(r'^get_email/', interface.get_email),
    url(r'^get_project_list/', interface.get_project_list),
    url(r'^get_db/', interface.get_db),
    url(r'^save_db/', interface.save_db),
    url(r'^delete_env/', interface.delete_env),
]
