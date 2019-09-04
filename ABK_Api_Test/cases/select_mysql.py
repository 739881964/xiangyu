import pymysql
from scripts.mysql_class import mysql


if __name__ == '__main__':
    sql = "select taskId from  where taskname = '分段重点语句20190717';"
    res = mysql.run_sql(sql)
