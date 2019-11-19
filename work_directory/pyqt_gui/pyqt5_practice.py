# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/19 14:38
# @Author  : Xiang Yu
# @File    : pyqt5_practice.py
# @Software: PyCharm
# @Company : BEIJING INTENGINE


import sys
import serial
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import QMainWindow, QApplication, QTextEdit, QAction, QFileDialog, QMessageBox, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog
from PyQt5 import QtCore


class SetButton(object):
    # 设置按钮
    def __init__(self):
        pass

    def set_button(self, name, width, high, method=None):
        # 设置确认，退出按钮
        btn = QPushButton(name, self)
        eval(f"btn.clicked.connect(QCoreApplication.instance().{method})")
        btn.resize(btn.sizeHint())
        # 设置退出按钮大小
        btn.move(width, high)


class QTCore(object):
    pass


class MyWindow(QtWidgets.QWidget, SetButton):
    _port = list(map(lambda x: str(x), list(range(1, 30))))

    def __init__(self):
        super(MyWindow, self).__init__()
        self.myButton = QtWidgets.QPushButton(self)
        self.myButton.setObjectName("my_button")
        self.myButton.setText("选择文件/*.bin")
        self.myButton.clicked.connect(self.select_file)
        self.myButton.move(20, 15)
        self.comboBox = QtWidgets.QComboBox(self)
        # self.comboBox.setObjectName('my_port')
        # self.comboBox.setEditText('port')
        self.comboBox.addItems(MyWindow._port)
        self.comboBox.setCurrentIndex(0)  # 设置默认值
        self.comboBox.currentText()  # 获得当前内容
        self.comboBox.move(22, 60)
        self.init_ui(self)

    def get_port(self):
        pass

    def init_ui(self, form):
        port_label = '端口号'
        # 设置窗口的位置和大小
        self.setGeometry(200, 200, 900, 520)
        # 设置窗口的标题
        self.setWindowTitle('upgrade app')
        # 设置窗口的图标，引用图片
        self.setWindowIcon(QIcon(jpg_path))
        # 设置queen按钮
        self.set_button('确认', 690, 450, 'quit')
        # 设置退出按钮
        self.set_button('退出', 780, 450, 'quit')
        # 设置端口文本提示
        # _translate = QtCore.QCoreApplication.translate
        # self.setLayout(port_label)
        # self.set_button('端口', 50, 60, '')
        # 显示窗口
        self.show()

    def select_file(self):
        # directory = QFileDialog.getExistingDirectory(self, "选取文件夹", "./")  # 起始路径
        # print(directory)

        # 设置文件扩展名过滤,注意用双分号间隔
        all_file_name, file_type = QFileDialog.getOpenFileNames(self, "选取文件", "./",  "Text Files (*.bin)")

        for file in all_file_name:
            print(file)

        # file_name_2, file_type_2 = QtWidgets.QFileDialog.getOpenFileNames(self, "多文件选择", "/", "所有文件 (*);;文本文件 (*.bin)")
        #
        # for one_name, one_type in (file_name_2, file_type_2):
        #     print(one_name, one_type)

    def closeEvent(self, event):

        reply = QMessageBox.question(self, 'Message',
                                     "Are you sure to quit?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        # if reply == QtGui.QMessageBox.Yes:
        #     event.accept()
        # else:
        #     event.ignore()

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


class SetSerialPort(MyWindow):
    # 设置端口号
    def __init__(self):
        super(SetSerialPort, self).__init__()
        port = self.get_port()
        self.port = serial.Serial(port)
        if not self.port:
            self.port.open()

    def get_port(self):
        my_window = MyWindow()
        # my_port = my_window()
        return 1


if __name__ == "__main__":
    jpg_path = r'C:\Users\xiangyu\Desktop\image\Python.jpg'
    app = QtWidgets.QApplication(sys.argv)
    show = MyWindow()
    show.show()
    sys.exit(app.exec_())

