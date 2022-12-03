#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/29 19:39
# @Author  : buding
# @Site    : 
# @File    : logining.py
# @Software: PyCharm



from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Logining():

    def __init__(self, login_data, clientip):
        # 寻找是否已经存在该浏览器
        ds = {'platform': 'ANY',
              'browserName': login_data["browser_type"],
              'version': '',
              'javascriptEnabled': True
              }
        url = 'http://' + clientip + ':5577/wd/hub'
        self.driver = webdriver.Remote(url, desired_capabilities=ds)

        # if login_data["browser_type"] == "Chrome":
        #     self.driver = webdriver.Chrome()
        # elif login_data["browser_type"] == "Firefox":
        #     self.driver = webdriver.Firefox()
        # elif login_data["browser_type"] == "IE":
        #     self.driver = webdriver.Ie()
        # elif login_data["browser_type"] == "Edge":
        #     self.driver = webdriver.Edge()
        # elif login_data["browser_type"] == "Chrome_incognito_window":
        #     option = webdriver.ChromeOptions()
        #     option.add_argument('--incognito')  # 设置option参数为隐身模式
        #     self.driver = webdriver.Chrome(options=option)  # 调用带参数的谷歌浏览器
        # elif login_data["browser_type"] == "Firefox_incognito_window":
        #     option = webdriver.FirefoxOptions()
        #     option.add_argument('-private')
        #     self.driver = webdriver.Firefox(options=option)
        # elif login_data["browser_type"] == "IE_incognito_window":
        #     option = webdriver.IeOptions()
        #     option.add_argument("-InPrivate") # 启动隐身模式未实现
        #     # option.set_capability("InternetExplorerDriver.IE_SWITCHES", "-private")
        #     self.driver = webdriver.Ie(options=option)
        # else:
        #     return WindowsError()
        self.driver.get(login_data["login_url"])
        self.driver.maximize_window()
        self.username = login_data["username"]
        self.password = login_data["password"]

    def a163_com(self):
        try:
            frame1 = WebDriverWait(self.driver, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, "//iframe[@frameborder='0']")), message=u'元素加载超时!')
            self.driver.switch_to.frame(frame1)
            username = WebDriverWait(self.driver, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, "//input[@data-placeholder='邮箱帐号或手机号码']")), message=u'元素加载超时!')
            username.clear()
            username.send_keys(self.username)
            password = WebDriverWait(self.driver, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='输入密码' and @name='password']")), message=u'元素加载超时!')
            password.clear()
            password.send_keys(self.password)
            login = self.driver.find_element_by_id("dologin")
            js = 'arguments[0].click()'
            self.driver.execute_script(js, login)
            # login.click()  # 点击登录
        except NoSuchElementException as e:
            print(e.message)



if __name__ == '__main__':
    login_data = {'id': 5, 'login_name': 'a163_com', 'login_url': 'https://mail.163.com/', 'redirect': '', 'username': 'ning_testonly', 'password': '@ningzijing1', 'browser_type': 'Edge', 'close_window_method': 0, 'user_role': '', 'quarter': '', 'data_range': ''
, 'remark': ''}
    Logining(login_data).a163_com()