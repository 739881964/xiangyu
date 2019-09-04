#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# datetime:2019/8/31 11:18


import pytest
from selenium import webdriver
from pages.login_page import LoginPage


@pytest.fixture()
def init_web():
    driver = webdriver.Chrome()
    driver.implicitly_wait(20)
    login_page = LoginPage(driver)
    yield driver, login_page
    driver.quit()


@pytest.fixture(scope='class')
def init_class():
    print('haallll')
    yield
    print("finish")


@pytest.fixture()
def haha():
    print("hahha")
    yield 'abc', 123
    print("afterr hahhah ")
