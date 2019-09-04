# coding=utf-8
import pymysql
from scripts.get_cfg import config
import random


class MysqlManual(object):

    def __init__(self):
        self.conn = pymysql.connect(
                                    host=config.get_value('lemon', 'host'),
                                    user=config.get_value('lemon', 'user'),
                                    password=config.get_value('lemon', 'password'),
                                    port=config.get_int('lemon', 'port'),
                                    db=config.get_value('lemon', 'db'),
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
        head_mobile = ['136', '155', '163', '183', '187']
        end_mobile = ''.join(random.sample('0123456789', 8))
        all_mobile = head_mobile[random.randint(0, 4)] + end_mobile

        return all_mobile

    def is_exit(self, mobile):
        """
        判断号码是否存在
        :param mobile:
        :return:
        """
        sql = 'select MobilePhone from member where MobilePhone = %s;'
        if self.run_sql(sql, args=(mobile, )):
            return True
        else:
            return False

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

        return mobile[0]['MobilePhone']


mysql = MysqlManual()


if __name__ == '__main__':
    # mysql = MysqlManual()
    # print(mysql.get_no_exit_mobile())
    # print(mysql.get_exit_mobile())
    # mysql.close_db()
    # sqls = 'select Id from member where MobilePhone = 13625696627'
    sqls = "select Id from loan where MemberId = 103970 order by CreateTime desc limit 0, 1;"
    sql = 'select * from member where MobilePhone = 18374968215'
    # sqls = 'select * from loan;'
    re = mysql.run_sql(sql)
    print(re)
