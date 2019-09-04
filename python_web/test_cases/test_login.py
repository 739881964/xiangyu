#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# datetime:2019/8/20 21:17

import time
import unittest

# 预期结果和实际结果的比较。
# if 条件
# assert 断言
# unittest
# pytest
import pytest
from ddt import ddt, data
from selenium import webdriver

from data.login_data import user_info_error, user_info_invalidate
from pages.home_page import HomePage
from pages.login_page import LoginPage

# 某一个变量，某一个方法，某个类
# 依据 python 一切皆为对象

# 数据具体方式：根本就不重要
# 1、列表，
# 2，Excel, DoExcel
# 3，数据库，DoMysql, 读取数据库里面的测试数据
# 4，.txt 文件，
# 5, ini,
# 6, yaml
# 7,.py , 配置

# 公共， 前置条件：规则


# fixture 不能yield 任何的东西
@pytest.mark.usefixtures('haha')
@pytest.mark.login
# @ddt
class TestLogin():

    # @classmethod
    # def setUpClass(cls):
    #     cls.driver = webdriver.Chrome()
    #     cls.driver.implicitly_wait(20)
    #     cls.login_page = LoginPage(cls.driver)

    # @classmethod
    # def tearDownClass(cls):
    #     cls.driver.quit()
    #
    # def setUp(self):
    #     pass
    #
    #
    # def tearDown(self):
    #     # self.driver.quit()
    #     self.login_page.user_elem.clear()
    #     self.login_page.pwd_elem.clear()

    # @data(*user_info_error)
    # def test_login_1_error(self, user_info):
    #     """测试登录功能异常。
    #     """
    #     # ｛‘test_login_1_error’: 'error'｝
    #     self.login_page.login(user_info[0], user_info[1])
    #     error_msg_element = self.login_page.get_actual_result()
    #     # 逻辑上的重复
    #     self.assertEqual(error_msg_element.text, user_info[2])


    @pytest.mark.login
    # @data(*user_info_invalidate)
    @pytest.mark.parametrize('user_info', user_info_invalidate)
    def test_login_2_unvalidate(self, user_info, init_web, init_class):
        """没有授权的异常用例"""
        driver, login_page = init_web
        login_page.login(user_info[0], user_info[1])
        invalid_msg_element = login_page.get_invalidate_result()
        assert (invalid_msg_element.text == user_info[2])
        # self.assert

    # def test_login_2_success(self):
    #     self.login_page.login('18684720553', 'python')
    #     user_element = HomePage(self.driver).user_element
    #     self.assertEqual(user_element.text, '我的账号yuze')


if __name__ == '__main__':
    unittest.main()
