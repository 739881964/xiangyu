#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-09-04 22:23
# @Author  : Yu xiang
# @File    : login_page.py

from time import sleep
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class LoginPage(BasePage):

    """元素定位作为类属性，方便维护"""
    url = 'http://120.78.128.25:8765/Index/login.html'
    username_locator = (By.NAME, 'phone')
    password_locator = (By.NAME, 'password')
    login_button_locator = (By.CLASS_NAME, 'btn.btn-special')
    error_msg_locator = (By.CLASS_NAME, 'form-error-info')
    no_authority_msg_locator = (By.CSS_SELECTOR, '.layui-layer-content')

    @property
    def username_element(self) -> WebElement:
        """username"""
        return self.wait_presence_element(self.username_locator)

    @property
    def password_element(self) -> WebElement:
        """password"""
        return self.wait_presence_element(self.password_locator)

    @property
    def login_button(self) -> WebElement:
        """login button"""
        return self.wait_click_element(self.login_button_locator)

    def actual_result(self):
        """actual result"""
        return self.driver.find_element(*self.error_msg_locator)

    def current_url(self):
        return self.driver.current_url

    def get_no_auth_msg(self):
        """没有权限提示信息"""
        return self.driver.find_element(*self.no_authority_msg_locator)

    def login_pass(self, username, password):
        """login steps"""
        self.driver.get(self.url)
        self.clear_username_password()
        self.username_element.send_keys(username)
        self.password_element.send_keys(password)
        e = self.wait_click_element(self.login_button_locator)
        e.click()
        sleep(2)
        current_url = self.current_url()
        return current_url

    def login_error(self, username, password):
        self.driver.get(self.url)
        self.clear_username_password()
        self.username_element.send_keys(username)
        self.password_element.send_keys(password)
        e = self.wait_click_element(self.login_button_locator)
        e.click()

    def clear_username_password(self):
        self.username_element.clear()
        self.password_element.clear()
