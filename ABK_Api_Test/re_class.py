# coding=utf-8
import re


# \d数字 \D非数字
# \w字符 \W非字符
# \s特殊字符 空格 \S非特殊空格
# ？非贪婪(前面加范围)
# *匹配0或多次
# +匹配1或多次
# ？匹配0或1次(前面是字符)
# 边界匹配^开始 $结束
# .匹配除\n以外所有
data = '<div class="text"> 岗位描述：<br>1、参与在线架构设计和优化，支撑实时、大规模、高可靠系统的研发；<br>2、负责推荐、广告等系统的设计和优化，提升系统的灵活性、稳定性；<br>3、参与构建基础数据仓库、计算和传输平台，流式计算，离线挖掘系统，机器学习系统等；<br>岗位要求：<br>1、2年或以上相关工作经验，熟练掌握Java后台开发知识；<br>2、基础知识扎实，例如：数据结构、网络编程、多线程编程、分布式架构；<br>3、丰富的后台架构开发经验，例如：推荐系统、广告系统、搜索引擎等；<br>4、具备Redis、ElasticSearch、MongoDB，Spark、Kafka等组件开发经验者优先；<br>5、具备创新思维，在专利和论文方面积累较多经验者优先；<br>6、有责任心，沟通能力佳，抗压能力强，表达能力出众者优先；</div>'

res = re.sub('<(.*?)>', '', data)
print(res)