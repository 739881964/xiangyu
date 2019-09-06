from time import sleep
from scripts.text_manual import *
from scripts.base_path import *
from datetime import datetime, timedelta
from scripts.excel_manual import ExcelManual
from scripts.conf_manual import config
from warnings import simplefilter
# import sys
import threading
import time
simplefilter(action='ignore', category=FutureWarning)


excel = ExcelManual(EXCEL_PATH, 'Sheet1')


def command_str(data):
     commands = [] # get commands
     for i in data:
         res = i.replace('\n', '')
         commands.append(res)
     return commands


def get_command(data, n):
    commands = []  # get commands * n
    for i in data:
        res = i.replace('\n', '')
        commands.append(res)
    five_commands = n * commands
    return five_commands


def get_time_list(data):
    time_list = []  # get time set
    for i in data:
        all_time = re.findall('[[](.*)[.]', i)
        time_list.append(all_time[0])
    return time_list


def get_key(data, time):
    """find command depend on time"""
    for i in data:
        if time in i:
            key = get_zh(i)
            return key


def get_key_word(data):
    """get command depend on list"""
    keys = []
    for i in data:
        key_word = get_zh(i)
        keys.append(key_word[0])
    return keys


def get_time(data):
    """return wav datetime"""
    return datetime.strptime(data, "%Y-%m-%d %H:%M:%S")


def get_str_time(data):
    """get str-list"""
    return data.strftime('%Y-%m-%d %H:%M:%S')


def get_start_time_list(data):  # datetime-list
    """return wav broadcast start_time"""
    start_time_list = []
    for i in data:
        # time = compare_data[2::5][0]
        start_time_str = re.findall('[[](.*)[.]', i)[0]
        start_time = get_time(start_time_str)
        start_time_list.append(start_time)
    return start_time_list


def get_start_time_list_str(data):  # str-list
    """return wav broadcast start_time"""
    start_time_list_str = []
    for i in data:
        if re.findall('[[](.*)[.]', i):
            start_time_str = re.findall('[[](.*)[.]', i)[0]
            start_time_list_str.append(start_time_str)
    return start_time_list_str


def get_actual_time(time):
    """return wav broadcast start_time add five s"""
    return time + timedelta(minutes=1/12)


def get_res_count_data(data):
    """get Chinese depend on data where from res.log """
    _count_data = []
    for i in data:  # i is str
        __data = re.findall('[\u4e00-\u9fa5]+', i)
        if __data:
            _count_data.append(i)
    return _count_data


def get_last_wav(data):
    """get 240 wav"""
    wav_list = []
    for i in data:
        if re.findall('^D(.*?)wav$', i):
            res = re.findall('^D(.*?)wav$', i)
            resp = 'D' + res[0] + 'wav'
            wav_list.append(resp)

    get_wav = []  # get where circulate wav five times
    for i in range(len(wav_list)):
        if i % 2 == 0:
            get_wav.append(wav_list[i])

    last_wav = []
    for i in get_wav:
        if not re.findall('55.wav', i):
            last_wav.append(i)
    return last_wav


def get_all_time(data):
    """abandon time, if 240, return 240, else filter then return 240 time_list"""
    if len(data) == 240:
        return data
    else:
        five_time = data[12::49]
        all_start_time_list = []
        for i in data:
            if i not in five_time:
                all_start_time_list.append(i)  # 240
        return all_start_time_list


def count_run_time(func):
    """calculate run count time"""
    def run(*args, **kw):
        one_time = time.ctime()
        func(*args, **kw)
        print('[{} --- {}]'.format(one_time, time.ctime()))
    return run


@count_run_time
def test_01(*args, **kw):
    data = read_list_txt(COMMANDS_FILE)  # res.log file_data_to_list
    all_commands = get_command(data, 5)  # get commands where circulate times
    all_count_data = read_rstrip_data(RESULT_LOG)  # get log_content to_list
    count_data = get_res_count_data(all_count_data)  # get need res.log data

    all_compare_data = read_rstrip_data(COMPARE_FILE)  # get wav data to list
    require_wav = get_last_wav(all_compare_data)  # 240 wav

    all_time = get_start_time_list_str(all_compare_data)
    start_time = get_all_time(all_time)
    before_time = list(map(lambda x: get_time(x), start_time))  # 240 times

    all_res_time_list = get_time_list(count_data)  # get res.log time to list
    command_str = read_str_txt(COMMANDS_FILE)

    after_time = list(map(lambda x: get_actual_time(x), before_time))  # start time add five s
    after_time_str = list(map(lambda x: get_str_time(x), after_time))  # str-time-list

    print('Start first read_and_write excel operate ......')
    for i in range(0, len(before_time)):  # circulate 240 times
        # for i in range(3):
        for j in all_res_time_list:
            time = get_time(j)
            # res_list = []
            if after_time[i] > time > before_time[i]:
                # print(time)
                key = get_key(count_data, j)[0]
                if key == all_commands[i]:
                    excel.write_data(i+2, require_wav[i], before_time[i], all_commands[i], j, key, config.get_value('res', 'success_res'))
                else:
                    excel.write_data(i+2, require_wav[i], before_time[i], all_commands[i], j, key, config.get_value('res', 'fail_res'))
                    log.error('error command is : {} expected command is : {}'.format(all_commands[i], key))
    print('First write success!!!')
    # the_row, wav_name=None, start_time=None, expected_command=None, reback_command=None, signel=None
    sleep(1)
    print('Second write to excel ...')
    read_data = excel.read_data()
    for i in range(0, len(read_data)):
        _data = read_data[i]['wav_name']
        _time = before_time[i]
        if _data is None:
            # print(_time)
            excel.write_data(i+2, require_wav[i], before_time[i], all_commands[i], '', '', config.get_value('res', 'no_res'))
    print('Second write success!!!')
    sleep(1)

    print('Start calculate right rate...')
    res_data = excel.read_data()
    count_mei = res_data[12::48]  # where xiaomei
    right = []
    error = []
    null = []
    for i in range(len(count_mei)):
        if count_mei[i]['reback_command'] == '你好小美':
            right.append(count_mei[i]['reback_command'])
        elif count_mei[i]['reback_command'] == '':
            null.append('lost')
        else:
            error.append(count_mei[i]['reback_command'])
    re_right = []
    re_error = []
    re__null = []
    else_list = []
    for k in res_data:
        if k not in count_mei:
            else_list.append(k)
    for j in range(len(else_list)):
        if else_list[j]['signel'] == 'Pass':
            re_right.append(1)
        elif else_list[j]['signel'] == 'Error':
            re_error.append(2)
        else:
            re__null.append(3)
    awake_rate = len(right) / 5 * 100  # wake_rate
    recognition_rate = len(re_right) / 235 * 100  # recognition rate
    false_recognition = len(re_error) / 235 * 100  # error rate
    un_recognition_rate = len(re__null) / 235 * 100  # uncertainly rate
    print('count end！result is：')
    print(
          '唤醒:', 5, ' R:', len(right), ' E:', len(error), ' L:', len(null),
          '\n识别:', 235, ' R:', len(re_right), ' E:', len(re_error), ' L:', len(re__null),
          '\n唤醒率是: %.2f' % awake_rate + '%',
          '\n识别率是: %.2f' % recognition_rate + '%',
          '\n误识率是: %.2f' % false_recognition + '%',
          '\n未识别率是: %.2f' % un_recognition_rate + '%'
          )
    # [2019-08-23 16:31:42.556] app_i2s_startPlay - invalid WAV!


def main():
    """function where add threading"""
    t = threading.Thread(target=test_01)
    t.start()


if __name__ == '__main__':
    main()
