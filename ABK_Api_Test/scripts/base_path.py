# coding=utf-8
import os


# 项目根目录路径
BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 数据路径
DATAS_PATH = os.path.join(BASE_PATH, 'datas')
TEST_DATAS_EXCEL_PATH = os.path.join(DATAS_PATH, 'excel_open_2.xlsx')

# 配置文件路径
CONFS_PATH = os.path.join(BASE_PATH, 'confs')
CONFS_FILE_PATH = os.path.join(CONFS_PATH, 'test.cfg')
USER_CONF_FILE_PATH = os.path.join(CONFS_PATH, 'test_01.cfg')

# 日志路径
LOGS_PATH = os.path.join(BASE_PATH, 'logs')
LOGS_FILE_PATH = os.path.join(LOGS_PATH, 'log.txt')

# 用例路径
CASES_PATH = os.path.join(BASE_PATH, 'cases')

# 报告路径
REPORTS_PATH = os.path.join(BASE_PATH, 'reports')
