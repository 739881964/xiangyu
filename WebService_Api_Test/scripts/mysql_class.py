# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author:xiangyu
# phone：19942429056
# datetime:2019/9/4 10:45
# software: PyCharm


import pymysql
from scripts.get_cfg import config
import random


class MysqlManual(object):
    """
    mysql数据库检验操作
    """
    def __init__(self):
        self.conn = pymysql.connect(
                                    host=config.get_value('lemon', 'host'),
                                    user=config.get_value('lemon', 'user'),
                                    password=config.get_value('lemon', 'password'),
                                    port=config.get_int('lemon', 'port'),
                                    # db=config.get_value('lemon', 'db'),
                                    charset=config.get_value('lemon', 'charset'),
                                    cursorclass=pymysql.cursors.DictCursor
                                    )

        self.cursor = self.conn.cursor()

    def run_sql(self, sql, args=None, is_more=False):
        self.cursor.execute(sql, args)  # 执行sql语句
        self.conn.commit()  # 数据库提交

        if is_more:
            res = self.cursor.fetchall()
        else:
            res = self.cursor.fetchone()

        return res

    def close_db(self):
        self.cursor.close()
        self.conn.close()

    @staticmethod
    def get_random_mobile():
        """
        创建一个随机号码
        :return:
        """
        head_mobile = ['132', '158', '168', '187', '189']
        end_mobile = ''.join(random.sample('0123456789', 8))
        all_mobile = head_mobile[random.randint(0, 4)] + end_mobile

        return all_mobile

    def is_exit(self, mobile):
        """
        判断号码是否存在数据库
        :param mobile:
        :return:
        """
        sql = 'select MobilePhone from member where MobilePhone = %s;'
        if self.run_sql(sql, args=(mobile, )):
            return True
        else:
            return False

    def webservice_mobile_is_exit(self, mobile):
        """
        判断webservice数据库是否存在随机生成的手机号
        :param mobile:
        :return:
        """
        end_two_num = mobile[-2:]
        last_third_num = mobile[-3:-2]
        sql = f'select Fmobile_no from sms_db_{end_two_num}.t_mvcode_info_{last_third_num} where Fmobile_no = %s;'
        if self.run_sql(sql, args=(mobile, )):
            return True
        else:
            return False

    def get_webservice_not_exit_mobile(self):
        """
        随机生成一个数据库不存在的手机号
        :return:
        """
        mobile = self.get_random_mobile()
        if not self.webservice_mobile_is_exit(mobile):
            return mobile
        else:
            self.get_webservice_not_exit_mobile()

    def get_no_exit_mobile(self):
        """
        创建一个不存在的手机号码
        :return:
        """
        mobile = self.get_random_mobile()
        if not self.is_exit(mobile):
            return mobile
        else:
            self.get_no_exit_mobile()

    def get_exit_mobile(self):
        """
        从数据库获取一个存在手机号码
        :return:
        """
        sql = 'select MobilePhone from member LIMIT 0, 1;'
        mobile = self.run_sql(sql)

        return mobile['MobilePhone']


if __name__ == '__main__':
    mysql = MysqlManual()
    print(mysql.get_webservice_not_exit_mobile())
