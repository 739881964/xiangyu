from scripts.text_manual import *
from scripts.base_path import *
import re


if __name__ == '__main__':
    data = read_list_txt(COMMANDS_FILE)
    commands = []  # 命令词
    for i in data:
        res = i.replace('\n', '')
        commands.append(res)

    for word in commands:
        pass

    # 无换行data_list
    compare_data = read_rstrip_data(COMPARE_FILE)
    # print(compare_data)
    wav_list = []
    for i in compare_data:
        if re.findall('^D(.*?)wav$', i):  # 获取所有音频
            res = re.findall('^D(.*?)wav$', i)
            resp = 'D' + res[0] + 'wav'
            wav_list.append(resp)

    get_wav = []
    for i in range(len(wav_list)):
        if i % 2 == 0:
            get_wav.append(wav_list[i])

    print(get_wav)

    pass

    # 实际结果log_list
    res_log_list = read_rstrip_data(RESUTL_LOG)

    des_res = read_str_txt(RESUTL_LOG)
    __len = get_zh(des_res)
    # print(len(__len))
