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
import random


class ParamsReplaces(object):

    config = ConfigClass(USER_CONF_FILE_PATH)
    mysql = MysqlManual()

    random_name = config.get_value('webservice', 'user_name') + str(random.randint(0, 2019))
    random_mobile = mysql.get_webservice_not_exit_mobile()
    pwd = config.get_value('webservice', 'pwd')
    mobile = config.get_value('send_mobile', 'mobile')
    # error_mobile = mysql.get_random_mobile() + str(random.randint(0, 2019))
    random_true_name = config.get_value('webservice', 'true_name') + str(random.randint(2019, 9999))
    # random_true_name = '余翔'
    cre_id = '342921199411212333'
    uid = None
    end_two_num = None
    third_num = None
    mes_code = None
    sql_mobile = None
    exit_name = None


def params_replace(data):
    param = re.compile('#(.*?)#')

    while param.search(data):
        expected = param.search(data)
        key = expected.group(1)
        value = getattr(ParamsReplaces, key)
        data = param.sub(value, data, count=1)

    return data


if __name__ == '__main__':
    # params = '{"name": "#invest_tel#", "pwd": "#invest_pwd#"}'
    # print(params_replace(params))
    params = '{"client_ip": "172.1.1.1", "tmpl_id": "1", "mobile": "#mobile#"}'
    print(params_replace(params))
