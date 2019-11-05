"""
此脚本是根据csv文件生成map文件，最终生成的map文件是用于浮点测试
和rtt所使用的格式
"""

import csv
import os


# 获取csv中文件内容,生成
def get_csv_con(file_path, _record_path_):
    wav_list = []
    with open(file_path, 'r') as csv_file:
        reader = csv.reader(csv_file)
        column = [row for row in reader][1:]
        for i in column:
            wav_name = i[1].rsplit('\\', 1)[1]
            wav_list.append(_record_path_ + '\\' + wav_name + ',' + i[0])
    return wav_list


# 生成浮点map
def get_float_map(_wav_list_):
    try:        
        with open(r'./float.map', 'a', encoding='utf-8') as fw:
            for i in _wav_list_:
                if '192.168.200.20' in i:
                    line = i.replace('\\', '/').split('/', 3)[3].replace(',', '\t').replace('.wav', '.pcm')
                    if _wav_list_[-1] != i:
                        fw.write('/' + line + '\n')
                    else:
                        fw.write('/' + line)
    except Exception as e:
        print('浮点生成map产生错误:', e)
        os.popen('pause')


# 生成rtt的map
def get_rtt_map(_wav_list):
    try:
        with open(r'./rtt.map', 'a', encoding='utf-8') as fw:
            for i in _wav_list:
                line = i.rsplit('\\', 1)[-1]
                fw.write(i.split(',')[1] + ' ' + line.replace('.wav', '.pcm').split(',')[0] + '\n')
    except Exception as e:
        print('rtt生成map产生错误:', e)
        os.popen('pause')


def compare_list(__record_path, __wav_list):
    record_set = set(os.listdir(__record_path))
    new_wav = []
    for i in __wav_list:
        wav_name = i.split(',')[0].rsplit('\\', 1)[1].replace('.wav', '.pcm')
        new_wav.append(wav_name)
    wav_set = set(new_wav)
    if len(wav_set-record_set) != 0:
        print('录音文件和csv文件有差异')
        os.popen('pause')


if __name__ == '__main__':
    filepath = input('请输入csv文件的路径和名称:(example:D:\\MIC_JD_AC_board_2019.09.01-08.06.59.csv)\n')
    record_path = input('请输入录音文件的路径:(example:\\192.168.200.20\\share\\Exchange\\jjli\\result_board_sound)\n')
    wav_list = get_csv_con(filepath, record_path)
    compare_list = (record_path, wav_list)
    get_float_map(wav_list)
    get_rtt_map(wav_list)
    print('OK,已经在本地生成两个文件')
    os.popen('pause')

