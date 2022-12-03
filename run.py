#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/1/30 8:11
# @Author  : buding
# @Site    : 
# @File    : run.py
# @Software: PyCharm
import os
import socket
# import assist.manage
from selenium import webdriver


def run():
    command = "python manage.py runserver 0.0.0.0:8080"
    os.system(command)
    hostname = socket.gethostname()
    ipaddr = socket.gethostbyname(hostname)
    driver = webdriver.Chrome()
    driver.get("http://"+ipaddr+":8080/assist_login/")
    driver.maximize_window()


if __name__ == '__main__':
    run()

#本程序适用于局域网内远程辅助登录，主要使用django和selenium搭建
# 本程序使用到selenium远程控制，需先建立主机与子机的注册连接
# 1/selenium-server-standalone-X.XX.jar和浏览器driver需要放在同一目录下
# 2/主机运用管理员权限，打开命令行，进入到selenium server所在的路径，运行：java -jar selenium-server-standalone-3.141.59.jar -role hub -port 5566，
# http://localhost:5566/grid/console网页可查看是否成功
# 3/子机运用管理员权限，打开命令行，到selenium server所在的路径，运行：java -jar selenium-server-standalone-3.141.59.jar -role node -hub http://主机IP:5566/grid/register/ -port 5577
# 4/子机访问http://主机IP:8080/assist_login/