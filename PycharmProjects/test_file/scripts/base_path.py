import os


# base目录
BASE_PATH = os.path.dirname(os.path.dirname(__file__))

# 数据文件目录
DATA_PATH = os.path.join(BASE_PATH, 'datas')
EXCEL_PATH = os.path.join(DATA_PATH, 'excel.xlsx')
TEXT_PATH = os.path.join(DATA_PATH, 'data.txt')

# 配置文件目录
CONF_PATH = os.path.join(BASE_PATH, 'confs')
CONF_FILE_PATH = os.path.join(CONF_PATH, 'test.cfg')

# 日志文件目录
LOG_PATH = os.path.join(BASE_PATH, 'logs')
LOG_FILE_PATH = os.path.join(LOG_PATH, 'test_log')

# file目录
FILES_PATH = os.path.join(BASE_PATH, 'files')
COMMANDS_FILE = os.path.join(FILES_PATH, 'commands.txt')
RESUTL_LOG = os.path.join(FILES_PATH, 'result.log')
COMPARE_FILE = os.path.join(FILES_PATH, 'compare2.log')

pass
