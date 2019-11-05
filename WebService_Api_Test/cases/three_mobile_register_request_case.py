# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author:xiangyu
# phone：19942429056
# datetime:2019/9/4 10:45
# software: PyCharm


from scripts.mysql_class import MysqlManual
from scripts.http_request_class import HttpRequest
from scripts.get_cfg import config
from scripts.base_path import USER_CONF_FILE_PATH


def create_three_tel(regname, pwd='yx201308'):

    http = HttpRequest()
    mysql = MysqlManual()

    url = config.get_value('start url', 'start_url') + '/member/register'
    sql = 'select Id from member where MobilePhone = %s'

    while True:
        mobile = mysql.get_no_exit_mobile()
        data = {'mobilephone': mobile, 'pwd': pwd, 'regname': regname}
        http.get_method('post', url, data=data)

        res = mysql.run_sql(sql, args=(mobile, ))
        if res:
            user_id = res['Id']
            break

    dict_data = {
        regname:
                {'user_id': user_id,
                 'mobilephone': mobile,
                 'pwd': pwd,
                 'regname': regname
                 }
}

    mysql.close_db()
    http.close_session()

    return dict_data


def generate_mobile():

    data = {}

    data.update(create_three_tel('invest_user'))
    data.update(create_three_tel('admin_user'))
    data.update(create_three_tel('borrow_user'))

    config.write_in_cfg(data, USER_CONF_FILE_PATH)  # 写入三个账号到配置文件


if __name__ == '__main__':
    generate_mobile()
