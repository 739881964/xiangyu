# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author:xiangyu
# phone：19942429056
# datetime:2019/9/4 10:45
# software: PyCharm


import unittest
# from libs.HTMLTestRunnerNew import HTMLTestRunner
from scripts.excel_class import ExcelClass
from libs.my_ddt import *
from scripts.get_cfg import config
from scripts.log_class import loger
from scripts.http_request_class import HttpRequest
from scripts.base_path import TEST_DATAS_EXCEL_PATH
from scripts.mysql_class import MysqlManual
# from scripts.params_replace import ParamsReplace
from scripts.parsmas_replace_to_data import ParamsReplaces, params_replace


excel = ExcelClass(TEST_DATAS_EXCEL_PATH, '投资')
case_name = excel.read_excel_all_data()


@ddt
class TestInvest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.mysql = MysqlManual()
        cls.http = HttpRequest()
        loger.info('------测试开始------')

    @data(*case_name)
    def test_invest(self, case):
        case_id = case['case_id']
        title = case['title']
        method = case['method']
        expected = case['expected']
        url = config.get_value('start url', 'start_url') + case['url']

        params = params_replace(case['params'])
        print(params)
        actual_res = (self.http.get_method(method, url, data=params))['msg']

        if '加标成功' == actual_res:
            check_sql = case['check_sql']
            if check_sql:
                check_sql = params_replace(check_sql)
                res = self.mysql.run_sql(check_sql)
                # print(res)
                setattr(ParamsReplaces, 'loan_id', str(res['Id']))

        msg = title + '---测试用例'
        success_msg = config.get_value('res', 'success_res')
        fail_msg = config.get_value('res', 'fail_res')

        try:
            self.assertEqual(expected, actual_res, msg=msg)
            loger.info('{} 的执行结果为: {}'.format(msg, success_msg))
            excel.write_data_in_excel(case_id+1, actual_res, success_msg)

        except AssertionError as e:
            print(msg, '不通过!')
            loger.error('{} 的执行结果为: {}, 失败的原因是: {}'.format(msg, fail_msg, actual_res))
            excel.write_data_in_excel(case_id+1, actual_res, fail_msg)
            raise e

    @classmethod
    def tearDownClass(cls):
        cls.mysql.close_db()
        cls.http.close_session()
        loger.info('------测试结束------')


if __name__ == '__main__':
    unittest.main()
