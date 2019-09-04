import os


# base dir
BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# dat file dir
DATA_PATH = os.path.join(BASE_PATH, 'datas')
EXCEL_PATH = os.path.join(DATA_PATH, 'excel_01.xlsx')
EXCEL_PATH_2 = os.path.join(DATA_PATH, 'excel_02.xlsx')
TEXT_PATH = os.path.join(DATA_PATH, 'data.txt')
PANDAS_DATA = os.path.join(DATA_PATH, 'pandas_data.xlsx')

# config dir
CONF_PATH = os.path.join(BASE_PATH, 'confs')
CONF_FILE_PATH = os.path.join(CONF_PATH, 'test.cfg')

# log file dir
LOG_PATH = os.path.join(BASE_PATH, 'logs')
LOG_FILE_PATH = os.path.join(LOG_PATH, 'test_log')

# file dir
FILES_PATH = os.path.join(BASE_PATH, 'files')
COMMANDS_FILE = os.path.join(FILES_PATH, 'commands.txt')
RESULT_LOG = os.path.join(FILES_PATH, 'result.log')
COMPARE_FILE = os.path.join(FILES_PATH, 'compare2.log')

pass
