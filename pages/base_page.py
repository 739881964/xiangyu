#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-09-04 21:47
# @Author  : Yu xiang
# @File    : base_page.py


import logging
from selenium.webdriver import Chrome
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from scripts.base_path import *
from datetime import datetime


class BasePage(object):

    def __init__(self, driver: Chrome):
        self.driver = driver

    def get_url(self):
        return self.driver.current_url

    def wait_click_element(self, locator):
        """until could click element"""
        return WebDriverWait(self.driver, 20).until(ec.element_to_be_clickable(locator))

    def wait_visible_element(self, locator):
        """element can be saw wait 20 s"""
        return WebDriverWait(self.driver, 20).until(ec.visibility_of_element_located(locator))

    def wait_presence_element(self, locator):
        """wait 20 s until element show"""
        try:
            return WebDriverWait(self.driver, 20).until(ec.presence_of_element_located(locator))
        except:
            logging.error('定位元素出错')
            self.save_screen_shot()

    def save_screen_shot(self):
        """take photos"""
        shot_name = LOG_IMG_DIR + '\\' + datetime.strftime(datetime.now(), "%Y-%m-%d %H:%M:%S") + '.png'
        self.driver.save_screenshot(shot_name)
