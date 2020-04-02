#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtWidgets import QVBoxLayout, QLabel, QHBoxLayout
from PyQt5.QtCore import pyqtSignal
import sys
from PyQt5.QtCore import QPoint, QRect, QSize, Qt
from PyQt5.QtWidgets import QApplication, QLayout, QSizePolicy, QWidget
from os import startfile


class FlowLayout(QLayout):

    def __init__(self, parent=None, margin=0, spacing=-1):
        super(FlowLayout, self).__init__(parent)
        if parent is not None:
            self.setContentsMargins(margin, margin, margin, margin)
        self.setSpacing(spacing)
        self.itemList = []

    def __del__(self):
        item = self.takeAt(0)
        while item:
            item = self.takeAt(0)

    def addItem(self, item):
        self.itemList.append(item)

    def count(self):
        return len(self.itemList)

    def itemAt(self, index):
        if 0 <= index < len(self.itemList):
            return self.itemList[index]

        return None

    def takeAt(self, index):
        if 0 <= index < len(self.itemList):
            return self.itemList.pop(index)

        return None

    def expandingDirections(self):
        return Qt.Orientations(Qt.Orientation(0))

    def hasHeightForWidth(self):
        return True

    def heightForWidth(self, width):
        height = self.doLayout(QRect(0, 0, width, 0), True)
        return height

    def setGeometry(self, rect):
        super(FlowLayout, self).setGeometry(rect)
        self.doLayout(rect, False)

    def sizeHint(self):
        return self.minimumSize()

    def minimumSize(self):
        size = QSize()

        for item in self.itemList:
            size = size.expandedTo(item.minimumSize())

        margin, _, _, _ = self.getContentsMargins()

        size += QSize(2 * margin, 2 * margin)
        return size

    def doLayout(self, rect, testOnly):
        x = rect.x()
        y = rect.y()
        lineHeight = 0

        for item in self.itemList:
            wid = item.widget()
            spaceX = self.spacing() + wid.style().layoutSpacing(QSizePolicy.PushButton,
                                                                QSizePolicy.PushButton, Qt.Horizontal)
            spaceY = self.spacing() + wid.style().layoutSpacing(QSizePolicy.PushButton,
                                                                QSizePolicy.PushButton, Qt.Vertical)
            nextX = x + item.sizeHint().width() + spaceX
            if nextX - spaceX > rect.right() and lineHeight > 0:
                x = rect.x()
                y = y + lineHeight + spaceY
                nextX = x + item.sizeHint().width() + spaceX
                lineHeight = 0

            if not testOnly:
                item.setGeometry(QRect(QPoint(x, y), item.sizeHint()))

            x = nextX
            lineHeight = max(lineHeight, item.sizeHint().height())

        return y + lineHeight - rect.y()


class ItemWidget(QWidget):

    def __init__(self, cover_type, movie_info=None, click_number=None, *args, **kwargs):
        super(ItemWidget, self).__init__(*args, **kwargs)
        self.cover_path = movie_info[cover_type]
        self.click_number = click_number
        self.number = movie_info['number']
        self.movie_path = movie_info['movie']
        self.Load()

    def Load(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(10, 20, 10, 0)
        # 图片label
        img = QImage(self.cover_path)  # 创建图片实例
        # print(img.width(), img.height())
        if img.width() > img.height():
            scale = 370 / img.width()  # 每次缩小20%
        else:
            scale = 200 / img.width()
        mgnWidth = int(img.width() * scale)
        mgnHeight = int(img.height() * scale)  # 缩放宽高尺寸
        size = QSize(mgnWidth, mgnHeight)
        pixImg = QPixmap.fromImage(img.scaled(size, Qt.IgnoreAspectRatio, Qt.SmoothTransformation))
        imageLabel = QLabel(self.number, self)
        imageLabel.resize(mgnWidth, mgnHeight)
        imageLabel.setPixmap(pixImg)

        layout.addWidget(imageLabel)
        # 片名和分数
        flayout = QHBoxLayout()
        flayout.addWidget(QLabel(self.number, self))
        layout.addLayout(flayout)

    def mouseDoubleClickEvent(self, QMouseEvent):  ##重载一下鼠标点击事件
        print("you clicked the label " + self.number)
        startfile(self.movie_path)


class ActorWidget(QWidget):

    def __init__(self, actor_name, actor_pic, *args, **kwargs):
        super(ActorWidget, self).__init__(*args, **kwargs)
        self.actor_name = actor_name
        self.actor_pic = actor_pic
        layout = QVBoxLayout(self)
        layout.setContentsMargins(10, 20, 10, 0)
        # 图片label
        img = QImage(actor_pic)  # 创建图片实例
        print(img.width(), img.height())
        scale = 180 / img.width()
        mgnWidth = int(img.width() * scale)
        mgnHeight = int(img.height() * scale)  # 缩放宽高尺寸
        size = QSize(mgnWidth, mgnHeight)
        pixImg = QPixmap.fromImage(img.scaled(size, Qt.IgnoreAspectRatio, Qt.SmoothTransformation))
        self.imageLabel = QLabel(actor_name, self)
        self.imageLabel.resize(mgnWidth, mgnHeight)
        self.imageLabel.setPixmap(pixImg)

        layout.addWidget(self.imageLabel)
        # 片名和分数
        flayout = QHBoxLayout()
        flayout.addWidget(QLabel(actor_name, self))
        layout.addLayout(flayout)

