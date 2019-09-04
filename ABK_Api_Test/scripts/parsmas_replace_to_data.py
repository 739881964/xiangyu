# coding=utf-8
import re
from scripts.mysql_class import MysqlManual
from scripts.base_path import USER_CONF_FILE_PATH
from scripts.get_cfg import ConfigClass


class ParamsReplaces(object):

    config = ConfigClass(USER_CONF_FILE_PATH)
    mysql = MysqlManual()

    not_exit_tel = mysql.get_no_exit_mobile()
    invest_tel = config.get_value('invest_user', 'mobilephone')
    invest_pwd = config.get_value('invest_user', 'pwd')
    borrow_id = config.get_value('borrow_user', 'user_id')
    admin_mobile = config.get_value('admin_user', 'mobilephone')
    admin_pwd = config.get_value('admin_user', 'pwd')
    invest_id = config.get_value('invest_user', 'user_id')
    loan_id = None


def params_replace(data):

    param = '#(.*?)#'
    while re.search(param, data):
        expected = re.search(param, data)
        key = expected.group(1)
        value = getattr(ParamsReplaces, key)
        data = re.sub(param, value, data, count=1)

    return data


if __name__ == '__main__':
    params = '{"name": "#invest_tel#", "pwd": "#invest_pwd#"}'
    print(params_replace(params))
    print(ParamsReplaces.not_exit_tel)
