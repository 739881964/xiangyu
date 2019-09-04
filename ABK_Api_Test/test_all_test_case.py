import unittest
from libs.HTMLTestRunnerNew import HTMLTestRunner
from scripts.base_path import CASES_PATH, REPORTS_PATH, USER_CONF_FILE_PATH
from datetime import datetime
import cases.test_three_mobile_register_request_case as test
import os


if __name__ == '__main__':

    # 存在配置文件就不注册三个账号
    if not os.path.exists(USER_CONF_FILE_PATH):
        test.generate_mobile()

    suite = unittest.defaultTestLoader.discover(CASES_PATH)
    result_path = REPORTS_PATH + '/' + datetime.strftime(datetime.now(), "%Y-%m-%d %H:%M:%S") + '.html'
    with open(result_path, 'wb') as f:
        runner = HTMLTestRunner(stream=f,
                                title='ABK接口测试报告',
                                description='ABK接口测试执行结果',
                                tester='余翔')
        runner.run(suite)
