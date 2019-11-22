# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/19 14:38
# @Author  : Xiang Yu
# @File    : upgrade_serial_port.py
# @Software: PyCharm
# @Company : BEIJING INTENGINE


import sys
import serial
import serial.tools.list_ports
from PyQt5.QtCore import QCoreApplication, Qt
from PyQt5.QtWidgets import (QMainWindow,
                             QApplication,
                             QTextEdit,
                             QAction,
                             QFileDialog,
                             QMessageBox,
                             QPushButton,
                             QLabel,
                             QFrame, QTextBrowser, QLineEdit)
from PyQt5.QtGui import QIcon
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog
from PyQt5 import QtCore


class SetButton(object):

    # 设置按钮
    def set_button(self, name, width, high, method=None):
        # 设置确认，退出按钮
        btn = QPushButton(name, self)
        eval(f"btn.clicked.connect(QCoreApplication.instance().{method})")
        btn.resize(btn.sizeHint())
        # 设置退出按钮大小
        btn.move(width, high)

        # return self

    # 设置标签
    def set_label(self, re_size_w, re_size_h, w, h, content=''):
        label = QLabel(self)
        label.resize(re_size_w, re_size_h)
        label.move(w, h)
        label.setFrameStyle(QFrame.Panel | QFrame.Sunken)
        label.setText(content)
        label.setAlignment(Qt.AlignBottom | Qt.AlignRight)


class MyWindow(SetButton):
    _port = list(map(lambda x: str(x), list(range(1, 30))))

    """
    def init(self):
        super(MyWindow, self).__init__()
        self.myButton = QtWidgets.QPushButton(self)
        self.myButton.setObjectName("my_button")
        self.myButton.setText("点击选择文件/*.bin")
        self.myButton.clicked.connect(self.select_file)
        self.myButton.move(20, 50)
        self.comboBox = QtWidgets.QComboBox(self)
        self.comboBox.setObjectName('my_port')
        self.comboBox.setEditText('port')
        self.comboBox.addItems(MyWindow._port)
        self.comboBox.setCurrentIndex(0)  # 设置默认值
        self.comboBox.currentText()  # 获得当前内容
        self.comboBox.move(22, 10)
        self.init_ui()
    """

    # def get_port(self):
    #     pass

    def init_ui(self):
        port_label = '端口号'
        # self.set_label.connect(self.file_name)
        self.setGeometry(200, 200, 900, 520)  # 设置窗口的位置和大小
        self.setWindowTitle('upgrade app')  # 设置窗口的标题
        self.setWindowIcon(QIcon(jpg_path))  # 设置窗口的图标，引用图片
        # self.set_button('确认', 690, 450)  # 设置queen按钮
        # self.set_button('确认', 690, 450, self).clicked.connect(self.click_button)

        self.set_button('退出', 780, 410, 'quit')  # 设置退出按钮
        # self.text_edit = QTextEdit()
        self.set_label(55, 20, 80, 10, '设置端口')

        # bin文件显示框
        self.text_browser_1 = QTextBrowser(self)
        self.text_browser_1.move(22, 100)
        self.text_browser_1.resize(200, 300)

        # 板子升级文件结果显示框
        self.text_browser_2 = QTextBrowser(self)
        self.text_browser_2.move(455, 20)
        self.text_browser_2.resize(400, 381)

        # 清除文本框
        btn_1 = QPushButton("清空文件", self)
        btn_1.move(22, 410)
        btn_1.resize(80, 20)
        # btn_1.clicked.connect(self)

        btn_2 = QPushButton('确认升级', self)
        btn_2.move(143, 410)
        btn_2.resize(80, 20)

        # self.show()  # 显示窗口

    def click_button(self):
        data = self.file_name()
        self.text_browser_1.setText(data)

    def file_name(self):
        files = self.select_file()
        file_list = list()
        for i in files:
            _file = i.split('/')[-1]
            file_list.append(_file)

        return '\n'.join(file_list)
        # self.text_edit.setPlainText('\n'.join(file_list))

    def select_file(self):
        # directory = QFileDialog.getExistingDirectory(self, "选取文件夹", "./")  # 起始路径
        # print(directory)
        # 设置文件扩展名过滤,注意用双分号间隔
        all_file_name, file_type = QFileDialog.getOpenFileNames(self, "选取文件", "./", "Text Files (*.bin)")
        all_file = []
        for file in all_file_name:
            _file = file.split('/')[-1]
            all_file.append(_file)

        self.text_browser_1.setText('\n'.join(all_file))

        # file_name_2, file_type_2 = QtWidgets.QFileDialog.getOpenFileNames(self, "多文件选择", "/", "所有文件 (*);;文本文件 (*.bin)")
        #
        # for one_name, one_type in (file_name_2, file_type_2):
        #     print(one_name, one_type)

        return all_file_name

    def closeEvent(self, event):

        reply = QMessageBox.question(self, 'Message',
                                     "Are you sure to quit?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

        # if reply == QtGui.QMessageBox.Yes:
        #     event.accept()
        # else:
        #     event.ignore()


class SetSerialPort(QtWidgets.QWidget, MyWindow):
    # 设置端口号
    _port_dict = {}

    def __init__(self):
        # object.__setattr__(SetSerialPort, '_port_dict', {})
        super(SetSerialPort, self).__init__()
        self.myButton = QtWidgets.QPushButton(self)
        self.myButton.setObjectName("my_button")
        self.myButton.setText("点击选择文件/*.bin")
        self.myButton.clicked.connect(self.select_file)
        self.myButton.move(20, 50)
        self.comboBox = QtWidgets.QComboBox(self)
        self.comboBox.setObjectName('my_port')
        self.comboBox.setEditText('port')
        self.comboBox.addItems(MyWindow._port)
        self.comboBox.setCurrentIndex(0)  # 设置默认值
        self.comboBox.currentText()  # 获得当前内容
        self.comboBox.move(22, 10)
        self.init_ui()

    def check_port(self):
        port_list = list(serial.tools.list_ports.comports())
        self.comboBox.clear()
        for port in port_list:
            self._port_dict["%s" % port[0]] = "%s" % port[1]
            self.comboBox.addItem(port[0])
            print(port)
        if len(port_list) == 0:
            self.comboBox.currentText('无串口')

        return port_list[0]


# set_ = SetSerialPort()
# set_.check_port()


if __name__ == "__main__":
    jpg_path = r'C:\Users\xiangyu\Desktop\image\Python.jpg'
    app = QtWidgets.QApplication(sys.argv)
    _show = SetSerialPort()
    _show.show()
    sys.exit(app.exec_())


