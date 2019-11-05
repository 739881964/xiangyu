***该框架仅适用日志分析统计，框架的紧密型较高，修改时注意其他的py脚本调用所产生的影响

目录：
1：confs：配置文件
2：datas：excel，txt等文件
3：files：存放音频log
4：log:目录scripts下log_manual.py封装的日志类，调用后代码产生的日志存放在此处
5：path：文件路径(可随意配置)
6：scripts：封装的一些统计用到的脚本，配置文件；excel(openpyxl和pandas)；日志；txt；线程等类


根目录下的py文件：
主要用到：
1：new_recognization_rate.py：分析并生成统计结果的主要脚本
2：new_normalize_script.py：音频归一化脚本
3：get_word_list_replace/by_process/threading:生成word_list脚本，threading/threadpool/asyncio效率极高，优先选用
4:其他脚本可自行分析

