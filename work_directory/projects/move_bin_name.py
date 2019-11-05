'''
本脚本是使用在串口测试时同步板卡录音,最后改变板卡录出bin文件名为原始文件名
而且将文件搬移到服务器中
'''

import os, glob, time
import datetime
import csv
import shutil


# 获取D盘中bin列表
def get_bin_list():
    bin_list = sorted(glob.glob(os.path.join(r'C:\Users\xiangyu\Desktop\bin', 'bach_*.bin')),
        key=lambda x: time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(os.path.getmtime(x))), reverse=False)
    return bin_list


# 获取wav名称
def get_bin_name():
    wav_list = []
    csv_name = sorted(glob.glob(os.path.join(r'D:\\', '*.csv')),
        key=lambda x: time.strftime("%Y-%m-%d %H:%M:%S",
            time.localtime(os.path.getctime(x))), reverse=True)[0]
    print(csv_name)
    with open(csv_name, 'r') as fr_csv:
        reader = csv.reader(fr_csv)
        column = [row for row in reader][1:]
        print(column)
        for i in column:
            wav_name = i[1].rsplit('\\', 1)[1]
            wav_list.append(wav_name)
    return wav_list


# 重新命名搬移到服务器\\192.168.200.20\share\Exchange\jjli\result_board_sound下按时间排序
if __name__ == '__main__':
    move_path = r'C:\Users\xiangyu\Desktop\123'
    now_time = time.strftime("%Y-%m-%d_%H-%M-%S", time.localtime())
    path = move_path + '\\' + now_time
    path1 = move_path + '\\备份_' + now_time 
    if os.path.exists(path) and os.path.exists(path1):
        print('已经存在文件夹')
    else:
        os.mkdir(path)
        os.mkdir(path1)
    bin_list = get_bin_list()
    wav_list = get_bin_name()
    con = 0
    for i in bin_list:
        shutil.copy(i, path1 + '\\')
        if 'bach_send.bin' == i.rsplit('\\', 1)[1]:
            shutil.move(i, path + '\\' + wav_list[con].split('.wav')[0] + '.bin')
            con += 1
        elif 'bach_send' + str(con) + '.bin' == i.rsplit('\\', 1)[1]:
            shutil.move(i, path + '\\' + wav_list[con].split('.wav')[0] + '.bin')
            con += 1

