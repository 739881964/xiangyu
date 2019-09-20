# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/19 16:51
# @Author  : Xiang Yu
# @File    : old_result.py
# @Software: PyCharm
# @Company : BEIJING INTENGINE
"""
注：
本脚本适合用于2019.08以后的新编译出的V1.之后的版本，对应的命令词索引有改变
本脚本是为了测试mic，其中主的是只播放wav，不做识别
其他的log是板子的识别情况
产生过程先产生总体的识别情况，之后生成list的log，在进行分析
data:2019.06.18
"""

from email.header import Header
import xlrd
import xlwt
import os
import glob
import time
import sys
import datetime
import smtplib
import chardet
from collections import Counter
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage


# 获取播放wav的log和识别log的列表
def get_log_name():
    slave_list = []
    log1 = sorted(glob.glob(os.path.join('D:\\', 'MIC_*.log')), 
                  key=lambda x: time.strftime("%Y-%m-%d %H:%M:%S", 
                                              time.localtime(os.path.getctime(x))), reverse=True)[0]
    log2 = sorted(glob.glob(os.path.join('D:\\', 'slave*.log')),
                  key=lambda x: time.strftime("%Y-%m-%d %H:%M:%S",
                                              time.localtime(os.path.getctime(x))), reverse=True)
    mic = log1.split('.log')[0].split('_')[-1].split('-')[0].replace('.', '-') \
          + ' ' + log1.split('.log')[0].split('_')[-1].split('-')[1].replace('.', ':')
    mic_time = datetime.datetime.strptime(mic, '%Y-%m-%d %H:%M:%S')
    for i in log2:
        slave = i.split('.log')[0].split('_')[-1].split('-')[0].replace('.', '-') \
                + ' ' + i.split('.log')[0].split('_')[-1].split('-')[1].replace('.', ':')
        slave_time = datetime.datetime.strptime(slave, '%Y-%m-%d %H:%M:%S')
        if (mic_time - slave_time).total_seconds() < 3600:
            slave_list.append(i)
    return log1, slave_list


# 如果有LIST，则使用该函数进行获取log之后分析得出结果
def get_list_log():
    log_list = sorted(glob.glob(os.path.join('D:\\', "*list*.log")),
                      key=lambda x: time.strftime("%Y-%m-%d %H:%M:%S",
                                                  time.localtime(os.path.getctime(x))), reverse=True)
    return log_list


# 发送邮件的主题的名字
def get_xls_list():
    filelist = []
    file = sorted(glob.glob(os.path.join('D:\\', '*.xls')), key=lambda x: time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(os.path.getctime(x))), reverse=True)
    nowtime = time.strftime("%Y-%m-%d-%H.%M.%S", time.localtime())
    now_time = datetime.datetime.strptime(nowtime, '%Y-%m-%d-%H.%M.%S')
    for i in file:
        name = i.split('\\')[1].split('.xls')[0].split('_')[-1]
        name_time = datetime.datetime.strptime(name, '%Y-%m-%d-%H.%M.%S')
        if (now_time - name_time).total_seconds() < 600:
            filelist.append(i)
    if 'XIAOMEI' in filelist[0]:
        name = '小美项目'
    elif 'XIAORUI' in filelist[0]:
        name = '小睿油烟机项目'
    elif 'XIAOYOU' in filelist[0]:
        name = '小优项目'
    elif 'XIAOKANGAC' in filelist[0]:
        name = '金都空调项目'
    elif 'XIAOKANGCURTAIN' in filelist[0]:
        name = '金都窗帘项目'
    elif 'FUQIANG' in filelist[0]:
        name = '富强净化器项目'
    elif 'SANXING' in filelist[0]:
        name = '三星产品项目'
    elif 'JIANFENG' in filelist[0]:
        name = '鉴丰蓝牙灯项目'
    elif 'TUOBANGXIAOMA' in filelist[0]:
        name = '拓邦马桶盖血压计项目'
    elif 'DIYUAN' in filelist[0]:
        name = '帝源空气净化器项目'
    elif 'TUOBANGZHINENGMATONG' in filelist[0]:
        name = '拓邦智能马桶项目'
    elif 'YUXIANQIUJIU' in filelist[0]:
        name = '安防场景遇险求救Demo项目'
    elif 'TONGYONGYUYINDENG' in filelist[0]:
        name = '通用型语音灯控项目'
    elif 'TONGYONGYUYINKONGTIAO' in filelist[0]:
        name = '通用型语音控制空调红外遥控器项目'
    elif 'XIAOKA' in filelist[0]:
        name = '小咖咖啡机项目'
    elif 'SIJIMUGE' in filelist[0]:
        name = '四季沐歌热水器项目'
    elif 'DAXIANJICHENGZAO' in filelist[0]:
        name = '达显集成灶'
    elif 'LAJIFENLEI' in filelist[0]:
        name = '语音分类垃圾桶'
    elif 'XIAODUGUI' in filelist[0]:
        name = '达显_消毒柜项目'
    elif 'ZHENGXIANG' in filelist[0]:
        name = '达显_蒸箱项目'
    return filelist, name


# 根据list分成多个listlog,根据返回值判断是否有多个播放的log
def get_mic_list(mic_filename, name):
    all_list = []
    with open(mic_filename, 'r') as fread:
        lines = fread.readlines()
        linesLine = []
        for line in lines:
            if '\n' == line or ' \n' == line:
                continue
            else:
                line = line.strip('\n')
                all_list.append(line)
    start = [i for i in range(len(all_list) - 1, -1, -1) if 'begin with' in all_list[i]][0]
    list_index = [i for i in range(start, len(all_list)) if 'LIST' in all_list[i]]
    if len(list_index) > 1:
        list_index.append(len(all_list) - 1)
    else:
        return
    list_group = []
    num = 1
    # print(list_index)
    for i in range(len(list_index) - 1):
        for j in range(num, len(list_index)):
            list_group.append([list_index[i], list_index[j]])
            num += 1
            break
    nowtime = time.strftime("%Y-%m-%d-%H.%M.%S", time.localtime())
    con = 0
    for m in list_group:
        con += 1
        with open(name + '_list' + str(con) + '_' + nowtime + '.log', 'w') as fwrite:
            fwrite.write(all_list[start] + '\n')
            for i in range(m[0], m[1]):
                fwrite.write(all_list[i] + '\n')
    return len(list_group)


# 获取播放时间log的列表
def get_play_time(filename, allWord):
    all_list = []
    wavlist = []
    totaldic = {}
    f = open(filename, 'rb')
    data = f.read()
    file_encoding = chardet.detect(data).get('encoding')
    f.close()
    try:
        with open(filename, 'r', encoding=file_encoding) as fread:
            lines = fread.readlines()
            linesLine = []
            for line in lines:
                if '\n' == line or ' \n' == line:
                    continue
                else:
                    line = line.strip('\n')
                    all_list.append(line)
        start = [i for i in range(len(all_list) - 1, -1, -1) if 'begin with' in all_list[i]][0]
        cont = 1
        for i in range(start, len(all_list)):
            if '<end>' not in all_list[i]:
                totaldic.setdefault(cont, []).append(all_list[i])
            else:
                totaldic.setdefault(cont, []).append('<end>')
                cont += 1
        for key in list(totaldic.keys()):
            for i in totaldic[key]:
                if 'nofile' in i:
                    del totaldic[key]
        for key, value in totaldic.items():
            for i in range(len(value)):
                for j in value:
                    if '[' in value[i] and ':' in value[i] and '.wav' in j and 'IET>' not in j and i == value.index(j) - 1:
                        wav_time = value[value.index(j) - 1] + j
                        while value[i].strip(' ') not in allWord:
                            # print(value[i])
                            i += 1
                        else:
                            wavlist.append(value[i] + ',' + wav_time)
                            break
                    elif '[' in value[i] and ':' in value[i] and '.wav' in j and 'IET>' in j and i == value.index(j):
                        wav_time = j
                        while value[i].strip(' ') not in allWord:
                            i += 1
                        else:
                            wavlist.append(value[i] + ',' + wav_time)
                            break
    except:
        print('读取主log(播放时间)出现问题')
        os.popen('pause')
    else:
        return wavlist


# 获取识别的列表
def del_slaver(filename):
    a_list = []
    f = open(filename, 'rb')
    data = f.read()
    file_encoding = chardet.detect(data).get('encoding')
    f.close()
    try:
        with open(filename, 'r', encoding=file_encoding) as fread:
            lines = fread.readlines()
            linesLine = []
            for line in lines:
                if '\n' == line:
                    continue
                elif 'isr_' in line:
                    line = line.strip('\n')
                    a_list.append(line)
                elif 'Version' in line:
                    ver = line.split('] ')[1]
    except:
        print('读取从log(识别log)出现问题')
        os.popen('pause')
    return a_list, ver


# 按照时间将播放和识别排序
def sortlist(timelist, wordlist):
    if not timelist:
        return wordlist
    if not wordlist:
        return timelist
    time_in = word_in = 0
    result = []
    while timelist and wordlist:
        if '\\' in timelist[time_in]:
            chang_time = timelist[time_in].replace('\\', '/')
            if 'IET>' in chang_time:
                a0 = chang_time.split(',')[1].split(' IET>//')[0]
            elif 'IET' not in chang_time:
                a0 = chang_time.split(',')[1].split(' //')[0]
        a1 = datetime.datetime.strptime(a0.strip('[').strip(']'), '%Y-%m-%d %H:%M:%S.%f')
        b0 = wordlist[word_in].split(' ')[0] + ' ' + wordlist[word_in].split(' ')[1]
        b1 = datetime.datetime.strptime(b0.strip('[').strip(']'), '%Y-%m-%d %H:%M:%S.%f')
        if a1 <= b1:
            result.append(timelist[time_in])
            timelist.pop(time_in)
        else:
            result.append(wordlist[word_in])
            wordlist.pop(word_in)
    if timelist:
        for i in timelist:
            result.append(i)
    if wordlist:
        for i in wordlist:
            result.append(i)
    return result


def write_log(allist, filename_2):
    nowtime = time.strftime("%Y-%m-%d-%H.%M.%S", time.localtime())
    name = '_'.join(filename_2.split('.')[0].split('_')[:-2])
    with open(name + '_' + nowtime + '.txt', 'w') as fwrite:
        for i in range(len(allist)):
            if ',' in allist[i]:
                wav = allist[i].strip(' ')
                fwrite.write(wav + '\n')
            else:
                fwrite.write(allist[i] + '\n')
    time.sleep(4)


# 处理最后生成的大列表WAV, ISR_WODE
def del_result(allist, allWord):
    dicnew = {}
    cont = 0
    wav_result = []
    # print(allist)
    for i in range(len(allist) - 1):
        if '.wav' in allist[i]:
            dicnew.setdefault(cont, []).append('<begin>')
            dicnew.setdefault(cont, []).append(allist[i].split(',')[0].strip(' '))
            if 'List' in allist[i + 1]:
                reco_index = allist[i + 1].split('st')[-1].split(']')[0].split('[')[-1]  # 获取的识别词的索引
                reco_sco = allist[i + 1].split('st')[-1].split(']')[1].split('[')[-1]  # 获取的分值
                word = allWord[int(allist[i + 1].split('st')[-1].split(']')[0].split('[')[-1]) - 1]
                wav = allist[i].split(',')[0].strip(' ')
                if word == wav:
                    add_str = 'right' + ',,,' + reco_sco
                    dicnew.setdefault(cont, []).append(add_str)
                    dicnew.setdefault(cont, []).append(allist[i].split(' ')[-1])
                    dicnew.setdefault(cont, []).append('<end>')
                    cont += 1
                else:
                    add_str = 'error,' + reco_index + ',' + allWord[int(reco_index) - 1] + ',' + reco_sco
                    dicnew.setdefault(cont, []).append(add_str)
                    dicnew.setdefault(cont, []).append(allist[i].split(' ')[-1])
                    dicnew.setdefault(cont, []).append('<end>')
                    cont += 1
            elif '.wav' in allist[i + 1]:
                dicnew.setdefault(cont, []).append('loss,,,')
                dicnew.setdefault(cont, []).append(allist[i].split(' ')[-1])
                dicnew.setdefault(cont, []).append('<end>')
                cont += 1
    if '.wav' in allist[-1]:
        cont += 1
        dicnew.setdefault(cont, []).append('<begin>')
        dicnew.setdefault(cont, []).append(allist[-1].split(',')[0].strip(' '))
        dicnew.setdefault(cont, []).append('loss,,,')
        dicnew.setdefault(cont, []).append(allist[-1].split(' ')[-1])
        dicnew.setdefault(cont, []).append('<end>')
    else:
        pass
    for value in dicnew.values():
        wav_word = value[1]
        wav_name = value[3]
        judge = value[2].split(',')[0]
        wav_result.append(wav_word)
        wav_result.append(wav_name)
        wav_result.append(judge)
        if judge == 'right':
            wav_result.append(wav_word)
        elif judge == 'loss':
            wav_result.append('nagetive')
        elif judge == 'error':
            wav_result.append(value[2].split(',')[2])
    return dicnew, wav_result


# 根据词表和生成的字典，进行正确错误和未识别的产生列表
def reco_dic(dic):
    LR = []
    LE = []
    LL = []
    for key, value in dic.items():
        if 'right' in value[2]:
            LR.append(value[1])
            sco = value[2].split(',')[-1]
            LR.append(sco)
        elif 'error' in value[2]:
            LE.append(value[1])
            sco = value[2].split(',')[-1]
            errval = value[2].split(',')[-2]
            LE.append(errval)
            LE.append(sco)
        elif 'loss' in value[2]:
            LL.append(value[1])
    return LR, LE, LL


# 处理识别错的词，得到字典 list1为识别词，list2为识别错误，list3为未识别
def recol_word(list1, list2, list3):
    dicword = {}
    for i in range(len(list1)):
        for j in range(0, len(list2) - 1, 3):
            if list1[i] == list2[j]:
                dicword.setdefault(list1[i], []).append(list2[j + 1])
        for m in range(len(list3)):
            if list3[m] == list1[i]:
                dicword.setdefault(list1[i], []).append('nagetive')
    return dicword


# 给生成的xls获得名
def get_new_name(filename_1, filename_2):
    if 'slave' in filename_2:
        mode = 'MIC_'
    else:
        mode = 'NO'
    if 'list' in filename_1.split('_')[-2].split('.')[0]:
        list_num = filename_1.split('_')[-2].split('.')[0]
    else:
        list_num = filename_2.rsplit('_', 2)[1]
    com = '_'.join(filename_2.split('\\')[1].split('.')[0].split('_')[:5])
    nowtime = time.strftime("%Y-%m-%d-%H.%M.%S", time.localtime())
    name = '_' + mode + com + '_' + list_num + '_' + nowtime + '.xls'
    return name


# 生成mic的xls文件
def get_xls(allWord, filename_1, filename_2):
    work_book = xlwt.Workbook(encoding='utf-8')
    borders = xlwt.Borders()  # 都有黑边框
    borders1 = xlwt.Borders()  # 右边框没有
    borders2 = xlwt.Borders()  # 左边框没有
    borders3 = xlwt.Borders()  # 左右都没有边框
    borders.left = xlwt.Borders.THIN
    borders1.left = xlwt.Borders.THIN
    borders.right = xlwt.Borders.THIN
    borders2.right = xlwt.Borders.THIN
    borders.top = xlwt.Borders.THIN
    borders1.top = xlwt.Borders.THIN
    borders2.top = xlwt.Borders.THIN
    borders3.top = xlwt.Borders.THIN
    borders.bottom = xlwt.Borders.THIN
    borders1.bottom = xlwt.Borders.THIN
    borders2.bottom = xlwt.Borders.THIN
    borders3.bottom = xlwt.Borders.THIN

    alignment = xlwt.Alignment()  # 对齐情况
    alignment.horz = xlwt.Alignment.HORZ_CENTER  # 水平对齐

    style = xlwt.XFStyle()  # 第一行格式,全黑边框，居中，宋体
    style1 = xlwt.XFStyle()  # 第一列格式,全黑边框，默认左对齐，宋体
    style2 = xlwt.XFStyle()  # 中间格式,只有上下边框，居中，宋体
    style3 = xlwt.XFStyle()  # 左中格式，右没有边框，居中，宋体
    style4 = xlwt.XFStyle()  # 右中格式，左没有边框，居中，宋体

    font = xlwt.Font()
    font.name = u'宋体'  # 字体设置成宋体

    style.font = font
    style1.font = font
    style2.font = font
    style3.font = font
    style4.font = font

    style.alignment = alignment
    style2.alignment = alignment
    style3.alignment = alignment
    style4.alignment = alignment

    style.borders = borders
    style1.borders = borders
    style2.borders = borders3
    style3.borders = borders1
    style4.borders = borders2

    # 创建了3个sheet
    sheet1 = work_book.add_sheet('recall')
    sheet2 = work_book.add_sheet('far')
    sheet3 = work_book.add_sheet('frr')
    sheet4 = work_book.add_sheet('right')
    sheet5 = work_book.add_sheet('error')
    sheet6 = work_book.add_sheet('wav_result')
    # 设置sheet1格式
    first_col = sheet1.col(0)  # 设置第一列的宽度xlwt中是行和列都是从0开始计算的
    first_col.width = 256 * 15
    # 设置第一列的宽度
    first_col1 = sheet1.col(0)
    first_col2 = sheet2.col(0)
    first_col3 = sheet3.col(0)
    first_col1.width = 256 * 15
    first_col2.width = 256 * 15
    first_col3.width = 256 * 15
    # 设置sheet2格式
    first_col = sheet2.col(0)
    first_col.width = 256 * 15
    sheet2.write(0, 0, 'labels', style1)
    sheet2.write(0, 1, 'TOTAL', style)
    sheet2.write(0, 2, 'FP', style)
    sheet2.write(0, 3, 'FAR', style)
    # 设置sheet3格式
    first_col.width = 256 * 15
    sheet3.write(0, 0, 'labels', style)
    sheet3.write(0, 1, 'TOTAL', style)
    sheet3.write(0, 2, 'FN', style)
    sheet3.write(0, 3, 'frr', style)
    sheet4.write_merge(0, 0, 0, 4, '各个词识别正确的得分情况', style)
    sheet5.write_merge(0, 0, 0, 4, '各个词识别错误的得分情况', style)
    sheet6.write(0, 0, '播放词')
    sheet6.write(0, 1, 'wav名称', style)
    sheet6.write(0, 2, '识别结果', style)
    sheet6.write(0, 3, '识别词', style)
    a = 1
    for i in range(0, 12):
        sheet3.write(0, i + 3 + a, '误识词' + str(a), style)
        sheet3.write(0, i + 4 + a, '误识率', style)
        a += 1
    # 写入sheet1的数据
    msg = filename_2.split('_')
    sheet1.write(1, 0, '板卡信息', style)
    sheet1.write(1, 1, msg[2], style)
    sheet1.write(1, 2, '板卡增益', style)
    sheet1.write_merge(1, 1, 3, 4, msg[4], style)
    sheet1.write_merge(2, 3, 0, 0, '词条', style)
    sheet1.write_merge(2, 2, 1, 4, 'overall', style)
    sheet1.write(3, 1, 'TOTAL', style)
    sheet1.write(3, 2, 'TP', style)
    sheet1.write(3, 3, 'FN', style)
    sheet1.write(3, 4, 'recall', style)

    wordlist, ver = del_slaver(filename_2)  # 获取slave的识别结果词
    wavList = get_play_time(filename_1, allWord)
    sheet1.write(0, 0, '版本信息', style)
    sheet1.write_merge(0, 0, 1, 4, ver, style)
    if wavList:
        result_sort = sortlist(wavList, wordlist)
        write_log(result_sort, filename_2)
        dicnew, wav_result = del_result(result_sort, allWord)
        LR, LE, LL = reco_dic(dicnew)
        Lrlen = len(LR) // 2
        Lelen = len(LE) // 3
        Lllen = len(LL)
        All = Lrlen + Lllen + Lelen
        wakeall = 0
        waketp = 0
        cmdtp = 0
        cmdall = 0
        cmdfp = 0
        for i in range(len(allWord)):
            if '你好nomi' == i:
                continue
            le = 0
            FP = 0
            TP = LR.count(allWord[i])
            re = 1  # 标记误识别的列数
            sheet5.write(1, i, allWord[i])

            for j in range(0, len(LE) - 1, 3):
                five_col = sheet5.col(i)
                five_col.width = 256 * 18
                if LE[j] == allWord[i]:
                    le += 1
                    re += 1
                    sheet5.write(re, i, LE[j + 1] + '     ' + LE[j + 2], style)
                if LE[j + 1] == allWord[i]:
                    FP += 1
            FN = le + LL.count(allWord[i])
            TOTAL = TP + FN
            # 进行了命令词和唤醒词的情况分类
            if 'XIAOMEI' in filename_1 or 'FUQIANG' in filename_1 or 'JIANFENG' in filename_1:
                if allWord[i] == '你好小美':
                    waketp += TP
                    wakeall += TOTAL
                else:
                    cmdtp += TP
                    cmdall += TOTAL
                    cmdfp += FP
            elif 'XIAORUI' in filename_1:
                if allWord[i] == '你好小睿' or allWord[i] == '小睿你好':
                    waketp += TP
                    wakeall += TOTAL
                else:
                    cmdtp += TP
                    cmdall += TOTAL
                    cmdfp += FP
            elif 'DAXIANJICHENGZAO' in filename_1:
                if allWord[i] == '森歌森歌' or allWord[i] == '达显达显':
                    waketp += TP
                    wakeall += TOTAL
                else:
                    cmdtp += TP
                    cmdall += TOTAL
                    cmdfp += FP

            elif 'XIAODUGUI' in filename_1:
                if allWord[i] == '森歌森歌' or allWord[i] == '达显达显':
                    waketp += TP
                    wakeall += TOTAL
                else:
                    cmdtp += TP
                    cmdall += TOTAL
                    cmdfp += FP

            elif 'ZHENGXIANG' in filename_1:
                if allWord[i] == '森歌森歌' or allWord[i] == '达显达显':
                    waketp += TP
                    wakeall += TOTAL
                else:
                    cmdtp += TP
                    cmdall += TOTAL
                    cmdfp += FP


            elif 'TONGYONGYUYINDENG' in filename_1:
                if allWord[i] == '你好小美' or allWord[i] == '智能管家' or allWord[i] == '你好小白' \
                        or allWord[i] == '小白你好':
                    waketp += TP
                    wakeall += TOTAL
                else:
                    cmdtp += TP
                    cmdall += TOTAL
                    cmdfp += FP
            elif 'TONGYONGYUYINKONGTIAO' in filename_1:
                if allWord[i] == '空调空调' or allWord[i] == '你好空调' or allWord[i] == '你好小美' \
                        or allWord[i] == '小康小康':
                    waketp += TP
                    wakeall += TOTAL
                else:
                    cmdtp += TP
                    cmdall += TOTAL
                    cmdfp += FP
            elif 'XIAOYOU' in filename_1:
                if allWord[i] == '小优小优':
                    waketp += TP
                    wakeall += TOTAL
                else:
                    cmdtp += TP
                    cmdall += TOTAL
                    cmdfp += FP
            elif 'XIAOKANGAC' in filename_1 or 'XIAOKANGCURTAIN' in filename_1:
                if allWord[i] == '小康小康':
                    waketp += TP
                    wakeall += TOTAL
                else:
                    cmdtp += TP
                    cmdall += TOTAL
                    cmdfp += FP
            elif 'DIYUAN' in filename_1:
                if allWord[i] == '你好帝源':
                    waketp += TP
                    wakeall += TOTAL
                else:
                    cmdtp += TP
                    cmdall += TOTAL
                    cmdfp += FP
            elif 'TUOBANGZHINENGMATONG' in filename_1:
                if allWord[i] == '智能马桶':
                    waketp += TP
                    wakeall += TOTAL
                else:
                    cmdtp += TP
                    cmdall += TOTAL
                    cmdfp += FP
            elif 'XIAOKA' in filename_1:
                if allWord[i] == '你好小咖':
                    waketp += TP
                    wakeall += TOTAL
                else:
                    cmdtp += TP
                    cmdall += TOTAL
                    cmdfp += FP
            elif 'SIJIMUGE' in filename_1:
                if allWord[i] == '小沐你好':
                    waketp += TP
                    wakeall += TOTAL
                else:
                    cmdtp += TP
                    cmdall += TOTAL
                    cmdfp += FP
            elif 'SANXING' in filename_1 or 'TUOBANGXIAOMA' in filename_1 or 'YUXIANQIUJIU' in filename_1 or 'LAJIFENLEI' in filename_1:
                waketp = 0
                wakeall = 0
                cmdtp += TP
                cmdall += TOTAL
                cmdfp += FP
            if TOTAL == 0:
                recall = 0
                frr = 0
            else:
                recall = '%.2f%%' % (TP / TOTAL * 100)
                frr = '%.2f%%' % (FN / TOTAL * 100)
            sheet1.write(i + 4, 0, allWord[i], style1)
            sheet1.write(i + 4, 1, TOTAL, style)
            sheet1.write(i + 4, 2, TP, style)
            sheet1.write(i + 4, 3, FN, style)
            sheet1.write(i + 4, 4, recall, style)
            if All == TOTAL:
                FAR = 0
            else:
                FAR = '%.2f%%' % (FP / (All - TOTAL) * 100)
            sheet2.write(i + 1, 0, allWord[i], style1)
            sheet2.write(i + 1, 1, All - TOTAL, style)
            sheet2.write(i + 1, 2, FP, style)
            sheet2.write(i + 1, 3, FAR, style)

            sheet3.write(i + 1, 0, allWord[i], style)
            sheet3.write(i + 1, 1, TOTAL, style2)
            sheet3.write(i + 1, 2, FN, style2)
            sheet3.write(i + 1, 3, frr, style4)
            for key, value in recol_word(allWord, LE, LL).items():
                if allWord[i] == key:
                    numdict = Counter(value)
                    numlist = numdict.most_common()
                    fr = 1
                    for n in range(len(numlist)):
                        if TOTAL == 0:
                            fw = 0
                        else:
                            fw = numlist[n][1] / TOTAL
                        sheet3.write(i + 1, 3 + n + fr, numlist[n][0], style4)
                        sheet3.write(i + 1, 4 + n + fr, fw, style4)
                        fr += 1
            sheet4.write(1, i, allWord[i])
            rr = 1
            for k in range(0, len(LR) - 1, 2):
                # 标记正确的列数
                four_col = sheet4.col(i)
                four_col.width = 256 * 18
                if allWord[i] == LR[k]:
                    rr += 1
                    sheet4.write(rr, i, LR[k + 1], style)
        sheet1.write(len(allWord) + 4, 0, '总计', style)
        sheet1.write(len(allWord) + 5, 0, '唤醒情况统计', style)
        sheet1.write(len(allWord) + 5, 1, wakeall, style)
        sheet1.write(len(allWord) + 5, 2, waketp, style)
        sheet1.write(len(allWord) + 5, 3, wakeall - waketp, style)
        if wakeall == 0:
            Rcall = 0
        else:
            Rcall = '%.2f%%' % (waketp / wakeall * 100)
        if cmdall == 0:
            cmdrcall = 0
        else:
            cmdrcall = '%.2f%%' % (cmdtp / cmdall * 100)
        if All == 0:
            cmdfar = 0
        else:
            cmdfar = FAR = '%.2f%%' % (cmdfp / All * 100)
        sheet1.write(len(allWord) + 5, 4, Rcall, style)
        sheet1.write(len(allWord) + 6, 0, '识别情况统计', style)
        sheet1.write(len(allWord) + 6, 1, cmdall, style)
        sheet1.write(len(allWord) + 6, 2, cmdtp, style)
        sheet1.write(len(allWord) + 6, 3, cmdall - cmdtp, style)
        sheet1.write(len(allWord) + 6, 4, cmdrcall, style)
        sheet1.write(len(allWord) + 4, 1, All, style)
        sheet1.write(len(allWord) + 4, 2, Lrlen, style)
        sheet1.write(len(allWord) + 4, 3, Lelen + Lllen, style)
        sheet1.write(len(allWord) + 4, 4, '%.2f%%' % (Lrlen / All * 100), style)
        sheet2.write(len(allWord) + 1, 0, '命令词误识别统计', style)
        sheet2.write(len(allWord) + 1, 1, All, style)
        sheet2.write(len(allWord) + 1, 2, cmdfp, style)
        sheet2.write(len(allWord) + 1, 3, cmdfar, style)
        y = 1
        x = 0
        for w in range(len(wav_result)):
            if x != 3:
                sheet6.write(y, x, wav_result[w], style)
                x += 1
            elif x == 3:
                sheet6.write(y, x, wav_result[w], style)
                y += 1
                x = 0
        name = get_new_name(filename_1, filename_2)
        if 'XIAOMEI' in filename_1:
            work_book.save(r'D:\XIAOMEI' + name)
        elif 'XIAORUI' in filename_1:
            work_book.save(r'D:\XIAORUI' + name)
        elif 'XIAOYOU' in filename_1:
            work_book.save(r'D:\XIAOYOU' + name)
        elif 'XIAOKANGAC' in filename_1:
            work_book.save(r'D:\XIAOKANGAC' + name)
        elif 'XIAOKANGCURTAIN' in filename_1:
            work_book.save(r'D:\XIAOKANGCURTAIN' + name)
        elif 'FUQIANG' in filename_1:
            work_book.save(r'D:\FUQIANG' + name)
        elif 'SANXING' in filename_1:
            work_book.save(r'D:\SANXING' + name)
        elif 'JIANFENG' in filename_1:
            work_book.save(r'D:\JIANFENG' + name)
        elif 'TUOBANGXIAOMA' in filename_1:
            work_book.save(r'D:\TUOBANGXIAOMA' + name)
        elif 'DIYUAN' in filename_1:
            work_book.save(r'D:\DIYUAN' + name)
        elif 'TUOBANGZHINENGMATONG' in filename_1:
            work_book.save(r'D:\TUOBANGZHINENGMATONG' + name)
        elif 'YUXIANQIUJIU' in filename_1:
            work_book.save(r'D:\YUXIANQIUJIU' + name)
        elif 'TONGYONGYUYINDENG' in filename_1:
            work_book.save(r'D:\TONGYONGYUYINDENG' + name)
        elif 'TONGYONGYUYINKONGTIAO' in filename_1:
            work_book.save(r'D:\TONGYONGYUYINKONGTIAO' + name)
        elif 'XIAOKA' in filename_1:
            work_book.save(r'D:\XIAOKA' + name)
        elif 'SIJIMUGE' in filename_1:
            work_book.save(r'D:\SIJIMUGE' + name)
        elif 'LAJIFENLEI' in filename_1:
            work_book.save(r'D:\LAJIFENLEI' + name)
        elif 'XIAODUGUI' in filename_1:
            work_book.save(r'D:\XIAODUGUI' + name)
        elif 'ZHENGXIANG' in filename_1:
            work_book.save(r'D:\ZHENGXIANG' + name)
    else:
        pass


# 设置发件人和接收人信息
def send_mail(list_file, _name):
    try:
        sender = 'tanjingtest@foxmail.com'  # '739881964@qq.com'  # 'xiangyu@intenginetech.com'  # 'tanjingtest@foxmail.com'
        password = 'ncydbifncdkbdehd'   # 'Yx201308'  # 'Intengine1'  # 'ncydbifncdkbdehd'  # 腾讯QQ邮箱或腾讯企业邮箱必须使用授权码进行第三方登陆
        receivers = ['slxie@intenginetech.com', 'xiangyu@intenginetech.com']
        '''
        receivers = [
            'hswang@intenginetech.com', 
            'weisun@intenginetech.com',
            'zjyan@intenginetech.com',
            'zytang@intenginetech.com',
            'yfwang@intenginetech.com'
        ]
        cc_mail = ['jjli@intenginetech.com']
        '''
        mail_host = 'smtp.qq.com'  # 腾讯服务器地址

        # #邮件正文
        content = '''
                  <p>Hello,各位好：</p>
                  <p>&emsp;&emsp;&emsp;最新测试结果见附件,如有问题及时沟通!</p>
                  '''

        message = MIMEMultipart()
        message.attach(MIMEText(content, 'html', 'utf-8'))  # 如果只发文本，用这个就够了。

        message['From'] = sender
        message['To'] = ','.join(receivers)
        # message['Cc'] = ','.join(cc_mail)
        subject = _name + '应用测试结果'
        message['Subject'] = subject
        for l in list_file:
            with open(l, 'rb') as f:
                mime = MIMEApplication(f.read())
                mime.add_header('Content-Disposition', 'attachment', file__name=l)
                message.attach(mime)
        sp = smtplib.SMTP_SSL(mail_host, 465)
        sp.login(sender, password)
        sp.sendmail(sender, receivers, str(message))  # receivers+cc_mail
        sp.quit()
    except smtplib.SMTPException:
        print('处理结果应该是成功,但是邮件发送失败')
        os.popen('pause')
    else:
        print('OK!')
        os.popen('pause')


# 设置发件人和接收人信息
def send_mail(filelist, name):
    try:
        sender = '739881964@qq.com'
        password = 'xilnonunqhlabcji'  # 腾讯QQ邮箱或腾讯企业邮箱必须使用授权码进行第三方登陆
        # receivers = ['yfwang@intenginetech.com']
        # #cc_mail = ['jjli@intenginetech.com']
        # mail_host = 'smtp.qq.com'

        receivers = ['yfwang@intenginetech.com']
        # receivers = ['hswang@intenginetech.com', 'weisun@intenginetech.com', 'zjyan@intenginetech.com',
        #              'zytang@intenginetech.com', 'yfwang@intenginetech.com', 'slxie@intenginetech.com', 'xiangyu@intenginetech.com',
        #            'xqzhang@intenginetech.com', 'jywei@intenginetech.com']
        # cc_mail = ['jjli@intenginetech.com']
        mail_host = 'smtp.qq.com'  # 腾讯服务器地址

        # #邮件正文
        content = '''
                  <p>Hello,各位好：</p>
                  <p>&emsp;&emsp;&emsp;最新测试结果见附件,如有问题及时沟通!</p>
                  '''

        message = MIMEMultipart()
        message.attach(MIMEText(content, 'html', 'utf-8'))  # 如果只发文本，用这个就够了。

        message['From'] = sender
        message['To'] = ','.join(receivers)
        # message['Cc'] = ','.join(cc_mail)
        subject = name + '应用测试结果'
        message['Subject'] = subject
        for i in filelist:
            with open(i, 'rb') as f:
                mime = MIMEApplication(f.read())
                mime.add_header('Content-Disposition', 'attachment', filename=i)
                message.attach(mime)
        smtp = smtplib.SMTP_SSL(mail_host, 465)
        smtp.login(sender, password)
        smtp.sendmail(sender, receivers, str(message))  # receivers + cc_mail
        smtp.quit()
    except smtplib.SMTPException:
        print('处理结果应该是成功,但是邮件发送失败')
        os.popen('pause')
    else:
        print('OK!')
        os.popen('pause')


if __name__ == '__main__':
    log1, log2 = get_log_name()
    if 'XIAOMEI' in log1:
        allWord = ['上下摆动', '中等风', '二十一度', '二十七度', '二十三度', '二十九度', \
                   '二十二度', '二十五度', '二十八度', '二十六度', '二十四度', '二十度', '你好nomi', \
                   '你好小美', '停止摆动', '关闭睡眠模式', '关闭空气清新', '关闭空调', '关闭节能模式', \
                   '关闭语音模式', '关闭除湿', '减小风速', '制冷模式', '制热模式', '十七度', '十九度', \
                   '十八度', '十六度', '升高一度', '升高五度', '增大风速', '定时一小时', '定时两小时', \
                   '左右摆动', '强劲风', '打开空调', '最大风', '最小风', '睡眠模式', '空气净化', \
                   '空气清新', '节能模式', '送风模式', '降低一度', '降低五度', '除湿模式', '风大点', \
                   '风小点', '高速风']
    elif 'XIAORUI' in log1:
        allWord = ['你好小睿', '小睿你好', '最大风量', '中等风量', '最小风量', '爆炒风量', '打开灯光', \
                   '关闭灯光', '关闭风机', '定时关机', '小睿关机']
    elif 'XIAOYOU' in log1:
        allWord = ['小优小优', '开启上升', '衣物挂好了', '我要晾衣服', '开启下降', '我要收衣服', \
                   '关闭上升', '关闭下降', '开启照明', '把灯打开', '关闭照明', '把灯关上', '开启风干', \
                   '打开风干', '关闭风干', '停止风干', '开启热风', '打开热风', '关闭烘干', '停止烘干', \
                   '开启消毒', '打开消毒', '关闭消毒', '停止消毒', '打开语音', '开启语音', '关闭语音', \
                   '声音大一点', '音量大一点', '声音小一点', '音量小一点', '要', '好的', '可以', '下降', \
                   '降下', '是', '降下来', '行', '没有问题', 'OK']
    elif 'XIAOKANGAC' in log1:
        allWord = ['小康小康', '开启空调', '关闭空调', '加热模式', '制冷模式', '除湿模式', \
                   '关闭除湿', '睡眠模式', '节能模式', '空气净化', '空气清新', '送风模式', '升高温度', \
                   '降低温度', '升高风速', '降低风速', '最小风', '最大风', '高速风', '中等风', '强劲风', \
                   '左右摆动', '上下摆动', '停止摆动', '十六度', '十七度', '十八度', '十九度', '二十度', \
                   '二十一度', '二十二度', '二十三度', '二十四度', '二十五度', '二十六度', '二十七度', \
                   '二十八度', '二十九度', '三十度', '恢复出厂设置']
    elif 'XIAOKANGCURTAIN' in log1:
        allWord = ['关闭灯光', '小康小康', '停止窗帘', '打开灯光', '打开窗帘', '关闭窗帘']
    elif 'FUQIANG' in log1:
        allWord = ['你好小美', '打开净化器', '关闭净化器', '调到一档', '调到二档', \
                   '调到三档', '智能模式']
    elif 'SANXING' in log1:
        allWord = ['airconditioneron', 'airconditioneroff', 'temperatureup', 'temperaturedown']
    elif 'JIANFENG' in log1:
        allWord = ['你好小美', '开灯', '请开灯', '关灯', '请关灯', '调亮一点', '再亮一点', \
                   '灯太暗', '调暗一点', '再暗一点', '灯太亮', '播放音乐', '暂停播放', '关闭声音', \
                   '打开声音', '上一曲', '上一首', '下一首', '下一曲', '调到一档', '调到二档', \
                   '调到三档', '调到四档', '增大音量', '减小音量', '音源切换']
    elif 'TUOBANGXIAOMA' in log1:
        allWord = ['小马播报血压', '增大音量', '减小音量', '开启播报', '关闭播报']
    elif 'DIYUAN' in log1:
        allWord = ['你好帝源', '开机', '关机', '请开机', '请关机', '调高档', '调低档']
    elif 'TUOBANGZHINENGMATONG' in log1:
        allWord = ['智能马桶', '开始冲水', '开始烘干', '开始便洗', '开始妇洗', '开始童洗', \
                   '开始宽幅', '运行停止', '水温一档', '水温二档', '水温三档', '水温四档', '水温五档', \
                   '水温关闭', '座温一档', '座温二档', '座温三档', '座温四档', '座温五档', '座温关闭', \
                   '风温一档', '风温二档', '风温三档', '风温四档', '风温五档', '风温关闭', '水压一档', \
                   '水压二档', '水压三档', '水压四档', '水压五档', '喷枪一档', '喷枪二档', '喷枪三档', \
                   '喷枪四档', '喷枪五档', '夜灯开启', '夜灯开', '夜灯关闭', '夜灯关', '测量体脂', \
                   '开启播报', '关闭播报', '开启节能', '关闭节能', '开启电源', '关闭电源']
    elif 'YUXIANQIUJIU' in log1:
        allWord = ['救命', '救命啊', '幺幺零', '着火了', '快跑', '杀人了', '啊啊啊']
    elif 'TONGYONGYUYINDENG' in log1:
        allWord = ['你好小美', '智能管家', '你好小白', '小白你好', '打开语音', '关闭语音', \
                   '打开声音', '关闭声音', '增大音量', '音量大一点', '减小音量', '音量小一点', '打开灯光', \
                   '开灯', '关闭灯光', '关灯', '调亮一点', '亮一点', '调暗一点', '暗一点', '调到最亮', \
                   '中等亮度', '调到最暗', '调到一档', '调到二档', '调到三档', '调到四档', '冷白光', \
                   '自然光', '暧色光', '改变颜色', '切换模式', '打开台灯', '关闭台灯', '打开卧室灯', \
                   '关闭卧室灯', '打开主卧灯', '关闭主卧灯', '打开客房灯', '关闭客房灯', '打开书房灯', \
                   '关闭书房灯', '打开阳台灯', '关闭阳台灯', '打开花园灯', '关闭花园灯', '打开厕所灯', \
                   '关闭厕所灯', '打开餐厅灯', '关闭餐厅灯 ', '打开吸顶灯', '关掉吸顶灯', '打开灯带', \
                   '关掉灯带', '打开廊灯', '关掉廊灯', '打开夜灯', '关闭夜灯', '定时关灯', '取消', \
                   '定时十分钟', '定时半小时', '定时一小时', '定时两小时']
    elif 'TONGYONGYUYINKONGTIAO' in log1:
        allWord = ['空调空调', '你好空调', '你好小美', '小康小康', '打开语音', '开启语音', \
                   '语音开', '关闭语音', '关掉语音', '语音关', '关闭语音模式', '打开声音', '关闭声音', \
                   '增大音量', '音量大一点', '声音大一点', '大声点', '大点声', '减小音量', '音量小一点', \
                   '声音小一点', '小声点', '小点声', '开启空调', '打开空调', '开启电源', '开机', '关闭空调', \
                   '关闭电源', '关机', '打开灯光', '请开灯', '开灯', '关闭灯光', '请关灯', '关灯', '关闭显示', \
                   '制冷模式', '清凉模式', '制热模式', '温暖模式', '送风模式', '自动模式', '智能模式', '空调自动', \
                   '全自动', '电加热', '加热模式', '关闭电加热', '除湿模式', '关闭除湿', '睡眠模式', '关闭睡眠模式', \
                   '节能模式', '关闭节能模式', '安静模式', '空气净化', '空气清新', '清新模式', '关闭空气清新', \
                   '温度升高', '升高温度', '调高温度', '升高一度', '调高一度', '温度降低', '降低温度', '调低温度', \
                   '降低一度', '调低一度', '升高五度', '降低五度', '十六度', '十七度', '十八度', '十九度', '二十度', \
                   '二十一度', '二十二度', '二十三度', '二十四度', '二十五度', '二十六度', '二十七度', '二十八度', \
                   '二十九度', '三十度', '三十一度', '三十二度', '增大风速', '升高风速', '调大风力', '风大点', \
                   '减小风速', '降低风速', '调小风力', '风小点', '最小风力', '最小风量', '最小风', '调到低档', '中等风', \
                   '中等风量', '调到中档', '最大风力', '最大风量', '最大风', '高速风', '强劲风', '调到高档', '自动风速', \
                   '自然风', '打开扫风', '打开摇头', '风扇摇头', '关掉扫风', '关闭摇头', '摇头停止', '停止摇头', \
                   '停止摆动', '打开上下扫风', '上下摆动', '关闭上下扫风', '打开左右扫风', '左右摆动', '关闭左右扫风', \
                   '取消', '定时十分钟', '定时二十分钟', '定时半小时', '定时一小时', '定时二小时', '定时两小时', \
                   '定时三小时', '定时四小时', '定时六小时', '定时八小时', '定时十小时', '查询状态', '查询帮助', \
                   '恢复出厂设置']
    elif 'XIAOKA' in log1:
        allWord = ['你好小咖', '拿铁', '美式']
    elif 'SIJIMUGE' in log1:
        allWord = ['小沐你好', '小沐开机', '请关机', '提高温度', '降低温度', '调为高档', \
                   '调为中档', '低档温度', '待机模式', '儿童模式', '成人模式', '老人模式', '智能模式', \
                   '增压功能', '冷水功能', '三十度', '三十一度', '三十二度', '三十三度', '三十四度', \
                   '三十五度', '三十六度', '三十七度', '三十八度', '三十九度', '四十度', '四十一度', \
                   '四十二度', '四十三度', '四十四度', '四十五度']
    elif 'DAXIANJICHENGZAO' in log1:
        allWord = ['森歌森歌', '达显达显', '打开低档', '打开小风', '打开低速', \
                   '打开中档', '打开中风', '打开中速', '打开高档', '打开大风', '打开高速', \
                   '关闭低档', '关闭小风', '关闭低速', '关闭中档', '关闭中风', '关闭中速', \
                   '关闭高档', '关闭大风', '关闭高速', '关闭风机', '关闭烟机', '打开照明', \
                   '打开灯光', '关闭照明', '关闭灯光', '打开消毒', '关闭消毒', '打开烘干', \
                   '关闭烘干', '打开自动', '关闭自动', '打开延时', '打开延迟', '关闭延时', \
                   '关闭延迟', '打开电源', '打开屏幕', '打开显示', '关闭电源', '关闭屏幕', \
                   '关闭显示', '返回上级', '返回上一步', '返回上一页', '打开音乐', '打开歌曲', \
                   '关闭音乐', '关闭歌曲', '打开视频', '关闭视频', '打开菜谱', '打开菜单', \
                   '关闭菜谱', '关闭菜单']
    elif 'LAJIFENLEI' in log1:
        allWord = ['502胶水', '优盘', '棒棒胶', '保健品', '保温杯', '报纸', \
                   '贝壳', '编织袋', '饼干', '玻璃', '菜叶', '餐巾纸', '茶叶', '茶叶渣', \
                   '尘土', '充电宝', '充电线', '宠物饲料', '创可贴', '创口贴', '瓷器', \
                   '打火机', '大骨头', '大肉', '蛋糕', '蛋壳', '灯管', '灯泡', '滴眼液', \
                   '电池', '电动玩具', '电路板', '调料', '调料瓶', '帆布袋', '干果仁', \
                   '干燥剂', '甘蔗皮', '瓜子皮', '果核', '果皮', '核桃壳', '红花油', \
                   '花卉', '花露水', '花生壳', '化妆品', '化妆品瓶', '积木', '鸡蛋', \
                   '鸡骨头', '坚果壳', '酱料', '胶带', '胶囊', '洁厕液', '金属制品', \
                   '镜子', '酒瓶', '旧包', '咖啡渣', '卡片', '口香糖', '口罩', '筷子', \
                   '矿泉水瓶', '零食', '螺丝刀', '绿植', '猫砂', '毛发', '毛巾', '棉签', \
                   '面包', '面膜', '木制品', '内衣', '尿不湿', '牛奶盒', '泡沫塑料', '泡腾片', \
                   '皮带', '皮鞋', '气泡袋', '气球', '铅笔', '巧克力', '染发剂', '杀虫剂', \
                   '剩菜', '剩饭', '湿巾纸', '食用油', '手机', '手套', '书本', '梳子', '鼠标', \
                   '树叶', '双面胶', '水彩笔', '水银温度计', '塑料', '塑料袋', '塑料盒', '塑料盆', \
                   '塑料瓶', '塑料玩具', '塑料碗', '糖果', '贴纸', '铁钉', '铁罐', '铁盒', '头发', \
                   '维生素', '卫生纸', '洗甲水', '虾壳', '相片', '香蕉皮', '橡皮泥', '消毒剂', '牙膏皮', \
                   '牙刷', '烟盒', '烟头', '颜料盒', '眼镜', '药片', '药品', '药品内包装', '药瓶', \
                   '药物', '一次性餐具', '衣服', '易拉罐', '饮料瓶', '油漆刷', '鱼骨头', '雨伞', \
                   '玉米皮', '玉米芯', '照片', '指甲', '指甲刀', '指甲油', '纸杯', '纸袋', '纸盒', \
                   '纸巾', '纸箱', '纸制品', '中性笔', '中药药渣', '竹牙签', '粽叶']

    elif 'XIAODUGUI' in log1:
        allWord = ['森歌森歌', '达显达显', '打开低档', '打开小风', '打开低速', '打开中档', '打开中风', \
                   '打开中速', '打开高档', '打开大风', '打开高速', '关闭低档', '关闭小风', '关闭低速', \
                   '关闭中档', '关闭中风', '关闭中速', '关闭高档', '关闭大风', '关闭高速', '关闭风机', \
                   '关闭烟机', '打开照明', '打开灯光', '关闭照明', '关闭灯光', '打开延时', '打开延迟', \
                   '关闭延时', '关闭延迟', '打开电源', '打开屏幕', '打开显示', '关闭电源', '关闭屏幕', \
                   '关闭显示', '返回上级', '返回上一步', '返回上一页', '打开音乐', '打开歌曲', '关闭音乐', \
                   '关闭歌曲', '打开视频', '关闭视频', '打开菜谱', '打开菜单', '关闭菜谱', '关闭菜单', \
                   '打开肉类', '打开鱼类', '打开蛋类', '打开糕点', '打开蹄筋', '打开蔬菜', '打开面食', \
                   '打开海鲜', '打开解冻', '停止工作', '结束工作', '开始工作', '暂停工作', '继续工作', \
                   '返回主页', '打开消毒', '关闭消毒', '打开烘干', '关闭烘干', '打开自动', '关闭自动']

    elif 'ZHENGXIANG' in log1:
        allWord = ['森歌森歌', '达显达显', '打开低档', '打开小风', '打开低速', '打开中档', '打开中风', \
                   '打开中速', '打开高档', '打开大风', '打开高速', '关闭低档', '关闭小风', '关闭低速', \
                   '关闭中档', '关闭中风', '关闭中速', '关闭高档', '关闭大风', '关闭高速', '关闭风机', \
                   '关闭烟机', '打开照明', '打开灯光', '关闭照明', '关闭灯光', '打开延时', '打开延迟', \
                   '关闭延时', '关闭延迟', '打开电源', '打开屏幕', '打开显示', '关闭电源', '关闭屏幕', \
                   '关闭显示', '返回上级', '返回上一步', '返回上一页', '打开音乐', '打开歌曲', '关闭音乐', \
                   '关闭歌曲', '打开视频', '关闭视频', '打开菜谱', '打开菜单', '关闭菜谱', '关闭菜单', \
                   '打开肉类', '打开鱼类', '打开蛋类', '打开糕点', '打开蹄筋', '打开蔬菜', '打开面食', \
                   '打开海鲜', '打开解冻', '停止工作', '结束工作', '开始工作', '暂停工作', '继续工作', \
                   '返回主页', '打开消毒', '关闭消毒', '打开烘干', '关闭烘干', '打开自动', '关闭自动']
    get_xls(allWord, log1, log2[0])

    try:
        for i in range(len(log2)):
            get_xls(allWord, log1, log2[i])
    except IndexError:
        print('确定跑的产品索引是从1开始,如果是从0开始的话请使用deal_mic.py或deal_mic.exe跑分析结果')
        os.popen('pause')
    finally:
        list_name = log1.split('.')[0]
        if get_mic_list(log1, list_name):
            log_num = get_mic_list(log1, list_name)
            log_list = get_list_log()    # 获取mic_list的列表
            for j in range(log_num):
                for m in range(len(log2)):
                    # print(log_list[j])
                    # print(log2[m])
                    get_xls(allWord, log_list[j], log2[m])
        else:
            pass
    time.sleep(5)
    try:
        filelist, name = get_xls_list()
    except IndexError:
        print("应该是没有产生xls结果文件,请查看主从文件名的时间是否超过1小时？")
        os.popen("pause")
    else:
        send_mail(filelist, name)
