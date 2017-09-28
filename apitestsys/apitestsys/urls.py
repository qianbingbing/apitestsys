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
    url(r'^addProject/', views.addProject),
    url(r'^projectList/', views.projectList),
    url(r'^addInterface/', views.addInterface),
    url(r'^addTestcase/', views.addTestcase),
    url(r'^interfaceList/', views.interfaceList),
    url(r'^testcaseList/', views.testcaseList),
    url(r'^commissonList/', views.commissonList),
    url(r'^reportList/', views.reportList),
    url(r'^reportDetail/', views.reportDetail),
    url(r'^save_project_base/', views.save_project_base),
    url(r'^get_project/', views.get_project),
    url(r'^save_project_env/', views.save_project_env),
]
