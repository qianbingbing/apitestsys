#!/usr/bin/python
# -*- coding: UTF-8 -*-
import MySQLdb
import re
from selenium import webdriver
import time
class GetSQL():
    def __init__(self):
        #将chromdriver 放在python27/script目录下
        #chromedriver = "E:\工作文件夹\UI自动化\chromedriver_win32\chromedriver.exe"
        #os.environ["webdriver.chrome.driver"] = chromedriver
        self.driver = webdriver.Chrome()
        #driver = webdriver.PhantomJS()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
    def login(self):
        driver = self.driver
        base_url = "http://wiki.nmtx.me/login.action"
        driver.get(base_url)
        driver.find_element_by_name("os_username").send_keys("qianbingbing")
        driver.find_element_by_name("os_password").send_keys("Hello123")
        driver.find_element_by_id("loginButton").click()
    def getsql(self):
        driver =self.driver
        url = 'http://wiki.nmtx.me/pages/viewpage.action?pageId=2950210'
        driver.get(url)
        driver.implicitly_wait(10)
        reg1 = r"use (.*);"
        reg2 = r"CREATE TABLE[^.;]*"
        html = driver.page_source
        dbre = re.compile(reg1)
        dblist = re.findall(dbre, html)
        print dblist
        for i in dblist:
            try:
                Mysql().cratebd(i)
            except:
                print "database CREATE error"
        '''
            for i in sqldivs:
            str = i.text
            reg1 = r"use (.*);"
            dbre = re.compile(reg1)
            dblist = re.findall(dbre, str)
            print dblist
            imgre = re.compile(reg2)
            imglist = re.findall(imgre, html)
            print imglist
            print len(imglist)
        '''

class Mysql():
    conn = MySQLdb.connect("tst-db1.nmtx.me", "qianbingbing", "KHrxDkbgqo",)
    cursor = conn.cursor()
    def cratebd(self,db_name):
        sql = "create database %s" % db_name
        self.cursor.execute(sql)

    def create_table(self):
        self.conn.select_db()
        # 创建数据表SQL语句
        sql=""""""
        try:
            self.cursor.executeBatch(sql)
        except:
            print "asdasd"
        # 关闭数据库连接
        self.conn.close()
if __name__ == '__main__':
    SQL = GetSQL()
    SQL.login()
    SQL.getsql()

