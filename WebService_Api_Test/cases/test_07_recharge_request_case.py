# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author:xiangyu
# phone：19942429056
# datetime:2019/9/4 10:45
# software: PyCharm


import unittest
from scripts.excel_class import ExcelClass
from libs.my_ddt import *
from scripts.get_cfg import config
from scripts.log_class import loger
from scripts.http_request_class import HttpRequest
from scripts.base_path import TEST_DATAS_EXCEL_PATH
from scripts.mysql_class import MysqlManual
# from scripts.params_replace import ParamsReplace
import json
from scripts.parsmas_replace_to_data import params_replace


excel = ExcelClass(TEST_DATAS_EXCEL_PATH, '充值')
case_name = excel.read_excel_all_data()


@ddt
class TestRecharge(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.mysql = MysqlManual()
        cls.http = HttpRequest()
        loger.info('------测试开始------')

    @data(*case_name)
    def test_recharge(self, case):
        case_id = case['case_id']
        title = case['title']
        method = case['method']
        expected = case['expected']  # int型
        params = params_replace(case['params'])
        url = config.get_value('start url', 'start_url') + case['url']

        check_sql = case['check_sql']
        if check_sql:
            check_sql = params_replace(check_sql)
            sql_data = self.mysql.run_sql(check_sql)
            before_amount = float(sql_data['LeaveAmount'])
            before_amount = round(before_amount, 2)

        code = (self.http.get_method(method, url, data=params))['code']  # str类型

        msg = title + '---测试用例'
        success_msg = config.get_value('res', 'success_res')
        fail_msg = config.get_value('res', 'fail_res')
        try:
            self.assertEqual(str(expected), code, msg=msg)
            if check_sql:
                check_sql = params_replace(check_sql)
                sql_data = self.mysql.run_sql(check_sql)
                after_amount = float(sql_data['LeaveAmount'])
                after_amount = round(after_amount, 2)

                actual_recharge_amount = int(after_amount - before_amount)
                # 实际充值金额,在excel的params中，字符串需转换成dict
                amount = json.loads(params)['amount']
                try:
                    self.assertEqual(amount, str(actual_recharge_amount))
                    loger.info('')
                except AssertionError as e:
                    loger.error('')
                    raise e

            loger.info('{} 的执行结果为: {}'.format(msg, success_msg))
            excel.write_data_in_excel(case_id+1, code, success_msg)

        except AssertionError as e:
            loger.error('{} 的执行结果为: {}, 失败的原因是: {}'.format(msg, fail_msg, code))
            excel.write_data_in_excel(case_id+1, code, fail_msg)
            raise e

    @classmethod
    def tearDownClass(cls):
        cls.mysql.close_db()
        cls.http.close_session()
        loger.info('------测试结束------')


if __name__ == '__main__':
    unittest.main()
