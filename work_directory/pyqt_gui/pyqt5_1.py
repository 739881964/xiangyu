# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/18 10:42
# @Author  : Xiang Yu
# @File    : pyqt5_1.py
# @Software: PyCharm
# @Company : BEIJING INTENGINE

"""
Py40.com PyQt5 tutorial

In this example, we create a simple
window in PyQt5.
"""

import sys

# 这里我们提供必要的引用。基本控件位于pyqt5.qtwidgets模块中。
from PyQt5.QtCore import Qt
from PyQt5.QtCore import QCoreApplication, QObject, pyqtSignal
from PyQt5.QtWidgets import (QApplication,
                             QWidget,
                             QToolTip,
                             QPushButton,
                             QDesktopWidget,
                             QGridLayout,
                             QSlider, QHBoxLayout, QVBoxLayout)

import sys
from PyQt5.QtWidgets import (QApplication,
                             QWidget,
                             QMessageBox)
from PyQt5.QtGui import QIcon, QFont, QPainter, QPen, QColor
from PyQt5.uic.properties import QtGui


jpg_path = r'C:\Users\xiangyu\Desktop\image\Python.jpg'


"""
class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.init_ui()  # 界面绘制交给InitUi方法

    def init_ui(self):
        # 设置窗口的位置和大小
        self.setGeometry(300, 300, 780, 500)
        # 设置窗口的标题
        self.setWindowTitle('Icon')
        # 设置窗口的图标，引用当前目录下的web.png图片
        self.setWindowIcon(QIcon(jpg_path))

        # 显示窗口
        self.show()
"""


"""
class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        # 这种静态的方法设置一个用于显示工具提示的字体。我们使用10px滑体字体。
        QToolTip.setFont(QFont('SansSerif', 10))

        # 创建一个提示，我们称之为settooltip()方法。我们可以使用丰富的文本格式
        self.setToolTip('This is a <b>QWidget</b> widget')

        # 创建一个PushButton并为他设置一个tooltip
        btn = QPushButton('Button', self)
        btn.setToolTip('This is a <b>QPushButton</b> widget')

        # btn.sizeHint()显示默认尺寸
        btn.resize(btn.sizeHint())

        # 移动窗口的位置
        btn.move(50, 50)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Tooltips')
        self.show()
"""


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        qbtn = QPushButton('Quit', self)
        qbtn.clicked.connect(QCoreApplication.instance().quit)
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(100, 100)

        self.setGeometry(300, 300, 780, 500)
        self.setWindowTitle('Quit button')
        self.show()


class _Example(QWidget):

    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):

        self.setGeometry(300, 300, 800, 520)
        self.setWindowTitle('Message box')
        self.show()

    def closeEvent(self, event):

        reply = QMessageBox.question(self, 'Message',
                                     "Are you sure to quit?", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)

        # if reply == QtGui.QMessageBox.Yes:
        #     event.accept()
        # else:
        #     event.ignore()
        #
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


"""
class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.resize(250, 150)
        self.center()

        self.setWindowTitle('Center')
        self.show()

    # 控制窗口显示在屏幕中心的方法
    def center(self):
        # 获得窗口
        qr = self.frameGeometry()
        # 获得屏幕中心点
        cp = QDesktopWidget().availableGeometry().center()
        # 显示到屏幕中心
        qr.moveCenter(cp)
        self.move(qr.topLeft())
"""


"""
class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):

        grid = QGridLayout()
        self.setLayout(grid)

        names = ['Cls', 'Bck', '', 'Close',
                 '7', '8', '9', '/',
                 '4', '5', '6', '*',
                 '1', '2', '3', '-',
                 '0', '.', '=', '+']

        positions = [(i, j) for i in range(5) for j in range(4)]

        for position, name in zip(positions, names):

            if name == '':
                continue
            button = QPushButton(name)
            grid.addWidget(button, *position)

        self.move(300, 150)
        self.setWindowTitle('Calculator')
        self.show()
"""


"""
class Communicate(QObject):
    updateBW = pyqtSignal(int)


class BurningWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.setMinimumSize(1, 30)
        self.value = 75
        self.num = [75, 150, 225, 300, 375, 450, 525, 600, 675]

    def setValue(self, value):

        self.value = value

    def paintEvent(self, e):

        qp = QPainter()
        qp.begin(self)
        self.drawWidget(qp)
        qp.end()

    def drawWidget(self, qp):

        font = QFont('Serif', 7, QFont.Light)
        qp.setFont(font)

        size = self.size()
        w = size.width()
        h = size.height()

        step = int(round(w / 10.0))

        till = int(((w / 750.0) * self.value))
        full = int(((w / 750.0) * 700))

        if self.value >= 700:

            qp.setPen(QColor(255, 255, 255))
            qp.setBrush(QColor(255, 255, 184))
            qp.drawRect(0, 0, full, h)
            qp.setPen(QColor(255, 175, 175))
            qp.setBrush(QColor(255, 175, 175))
            qp.drawRect(full, 0, till - full, h)

        else:

            qp.setPen(QColor(255, 255, 255))
            qp.setBrush(QColor(255, 255, 184))
            qp.drawRect(0, 0, till, h)

        pen = QPen(QColor(20, 20, 20), 1,
                   Qt.SolidLine)

        qp.setPen(pen)
        qp.setBrush(Qt.NoBrush)
        qp.drawRect(0, 0, w - 1, h - 1)

        j = 0

        for i in range(step, 10 * step, step):
            qp.drawLine(i, 0, i, 5)
            metrics = qp.fontMetrics()
            fw = metrics.width(str(self.num[j]))
            qp.drawText(i - fw / 2, h / 2, str(self.num[j]))
            j = j + 1


class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        sld = QSlider(Qt.Horizontal, self)
        sld.setFocusPolicy(Qt.NoFocus)
        sld.setRange(1, 750)
        sld.setValue(75)
        sld.setGeometry(30, 40, 150, 30)

        self.c = Communicate()
        self.wid = BurningWidget()
        self.c.updateBW[int].connect(self.wid.setValue)

        sld.valueChanged[int].connect(self.changeValue)
        hbox = QHBoxLayout()
        hbox.addWidget(self.wid)
        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)
        self.setLayout(vbox)

        self.setGeometry(300, 300, 390, 210)
        self.setWindowTitle('Burning widget')
        self.show()

    def changeValue(self, value):
        self.c.updateBW.emit(value)
        self.wid.repaint()
"""


if __name__ == '__main__':
    # 创建应用程序和对象
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


# if __name__ == '__main__':
#     # 每一pyqt5应用程序必须创建一个应用程序对象。sys.argv参数是一个列表，从命令行输入参数。
#     app = QApplication(sys.argv)
#     # QWidget部件是pyqt5所有用户界面对象的基类。他为QWidget提供默认构造函数。默认构造函数没有父类。
#     w = QWidget()
#     # resize()方法调整窗口的大小。这离是250px宽150px高
#     w.resize(550, 350)
#     # move()方法移动窗口在屏幕上的位置到x = 300，y = 300坐标。
#     w.move(300, 300)
#     # 设置窗口的标题
#     w.setWindowTitle('串口工具')
#     # 显示在屏幕上
#     w.show()
#
#     # 系统exit()方法确保应用程序干净的退出
#     # 的exec_()方法有下划线。因为执行是一个Python关键词。因此，exec_()代替
#     sys.exit(app.exec_())

