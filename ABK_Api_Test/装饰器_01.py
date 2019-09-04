# coding=utf-8
from datetime import datetime
import socket


def set_func(func):  # 闭包

    def one_func(*args, **kw):
        print(datetime.strftime(datetime.now(), "%Y-%m-%d %H:%M:%S"))
        return func(*args, **kw)

    return one_func


@set_func
def get_time(name, age):
    print('年龄:', age, '姓名:', name)


get_time(name='余翔', age=25)


def main():
    socket_user = socket.socket()
    pass


if __name__ == '__main__':
    main()
