# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author:xiangyu
# phone：19942429056
# datetime:2019/9/4 10:45
# software: PyCharm
import re
from scripts.mysql_class import MysqlManual
from scripts.base_path import USER_CONF_FILE_PATH
from scripts.get_cfg import ConfigClass


class ParamsReplace(object):

    not_exit_tel = r'\$\{not_exit_tel\}'
    invest_tel = r'\$\{invest_tel\}'
    invest_pwd = r'\$\{invest_pwd\}'
    borrow_id = r'\$\{borrow_id\}'
    admin_mobile = r'\$\{admin_mobile\}'
    admin_pwd = r'\$\{admin_pwd\}'
    invest_id = r'\$\{invest_id\}'
    loan_id_params = r'\$\{loan_id\}'

    config = ConfigClass(USER_CONF_FILE_PATH)

    @classmethod
    def not_exit_mobile(cls, data):

        mysql = MysqlManual()
        if re.search(cls.not_exit_tel, data):
            mobile = mysql.get_no_exit_mobile()
            data = re.sub(cls.not_exit_tel, mobile, data)
        mysql.close_db()

        return data

    @classmethod
    def exit_mobile(cls, data):

        mysql = MysqlManual()
        if re.search(cls.not_exit_tel, data):
            mobile = mysql.get_exit_mobile()
            data = re.sub(cls.not_exit_tel, mobile, data)
        mysql.close_db()

        return data

    @classmethod
    def invest_user_tel(cls, data):
        """
        替换成注册投资人号码
        :param data:
        :return:
        """

        if re.search(cls.invest_tel, data):
            mobile = cls.config.get_value('invest_user', 'mobilephone')
            data = re.sub(cls.invest_tel, mobile, data)

        return data

    @classmethod
    def invest_user_pwd(cls, data):
        """
        :param data:
        :return:
        """

        if re .search(cls.invest_pwd, data):
            pwd = cls.config.get_value('invest_user', 'pwd')
            data = re.sub(cls.invest_pwd, pwd, data)

        return data

    @classmethod
    def invest_user_id(cls, data):
        """
        :param data:
        :return:
        """

        if re .search(cls.invest_id, data):
            user_id = cls.config.get_value('invest_user', 'user_id')
            data = re.sub(cls.invest_id, user_id, data)

        return data

    @classmethod
    def borrow_user_id(cls, data):
        if re.search(cls.borrow_id, data):
            user_id = cls.config.get_value('borrow_user', 'user_id')
            data = re.sub(cls.borrow_id, user_id, data)

        return data

    @classmethod
    def admin_user_mobile(cls, data):
        if re.search(cls.admin_mobile, data):
            mobile = cls.config.get_value('admin_user', 'mobilephone')
            data = re.sub(cls.admin_mobile, mobile, data)

        return data

    @classmethod
    def admin_user_pwd(cls, data):
        if re.search(cls.admin_pwd, data):
            pwd = cls.config.get_value('admin_user', 'pwd')
            data = re.sub(cls.admin_pwd, pwd, data)

        return data

    @classmethod
    def load_id_params(cls, data):

        if re.search(cls.loan_id_params, data):
            loan_id = getattr(cls, 'loan_id')
            loan_id = str(loan_id)
            data = re.sub(cls.loan_id_params, loan_id, data)

        return data

    @classmethod
    def register_replace(cls, data):

        data = cls.not_exit_mobile(data)
        data = cls.invest_user_tel(data)

        return data

    @classmethod
    def login_replace(cls, data):

        data = cls.not_exit_mobile(data)
        data = cls.invest_user_pwd(data)
        data = cls.invest_user_tel(data)

        return data

    @classmethod
    def recharge_replace(cls, data):

        data = cls.invest_user_tel(data)
        data = cls.invest_user_pwd(data)
        data = cls.not_exit_mobile(data)

        return data

    @classmethod
    def add_loan_replace(cls, data):

        data = cls.admin_user_mobile(data)
        data = cls.admin_user_pwd(data)
        data = cls.borrow_user_id(data)

        return data

    @classmethod
    def invest_replace(cls, data):

        data = cls.admin_user_mobile(data)
        data = cls.admin_user_pwd(data)
        data = cls.invest_user_tel(data)
        data = cls.invest_user_pwd(data)
        data = cls.invest_user_id(data)
        data = cls.borrow_user_id(data)
        data = cls.load_id_params(data)

        return data


if __name__ == '__main__':
    params_replace = ParamsReplace()
    data_1 = '{"MobilePhone": "${MobilePhone}"}'
    # data_2 = '{"MobilePhone": "${MobilePhone}"}'
    print(params_replace.register_replace(data_1))
    # print(params_oneReplace().register(data_2))
