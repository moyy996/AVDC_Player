#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from configparser import ConfigParser

from AVDC_Player_Simple import Ui_MainWindow
from FlowLayout import FlowLayout, ItemWidget
from test import *
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTreeWidgetItem


class MyMAinWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(MyMAinWindow, self).__init__(parent)
        self.Ui = Ui_MainWindow()  # 实例化 Ui
        self.Ui.setupUi(self)  # 初始化Ui
        self.gLayout = FlowLayout(self.Ui.scrollAreaWidgetContents)
        self.media_list = self.Ui.treeWidget_media_list
        self.number = ''
        self.pic_type = ''
        self.path_library = ''
        self.path_movie = ''
        self.movie_type = ''
        self.total = {}
        self.Init()
        self.media_list.expandAll()

    def Init(self):
        self.Ui.treeWidget_media_list.clicked.connect(self.treeWidget_media_list_clicked)
        self.Load_config()
        self.library_lists()

    def Load_config(self):
        config_file = 'config.ini'
        config = ConfigParser()
        config.read(config_file, encoding='UTF-8')
        self.pic_type = config['pic']['pic_type']
        self.path_library = config['pic']['movie_path']
        self.movie_type = config['pic']['movie_type']

    def show_pic(self):
        # 删除原来的widget
        if self.gLayout.count() != 0:
            count_glayout_widget = self.gLayout.count() - 1
            for i in range(self.gLayout.count()):
                self.gLayout.itemAt(count_glayout_widget - i).widget().deleteLater()
        movie_list = self.total
        count = len(movie_list)
        if count == 0:
            self.statusBar().showMessage('加载完毕，共 0 个视频显示')
            return
        for movie in movie_list:
            itemWidget = ItemWidget(self.pic_type, movie_list[movie])
            movie_info = movie_list[movie]['movie_info']
            if movie_info != '':
                itemWidget.setToolTip(movie_info)
            self.gLayout.addWidget(itemWidget)
        self.statusBar().showMessage('加载完毕，共' + str(count) + '个视频')

    def treeWidget_media_list_clicked(self, qmodeLindex):
        self.statusBar().showMessage('正在加载')
        item = self.Ui.treeWidget_media_list.currentItem()
        parent = item.parent()
        # 获取当前节点的路径
        if parent is None:
            self.path_movie = os.path.join(self.path_library, item.text(0))
        else:
            self.path_movie = os.path.join(self.path_library, parent.text(0), item.text(0))
        try:
            self.movie_lists()
            self.show_pic()
        except Exception as error_info:
            print(error_info)

    def add_node(self, parent, str):
        node = QTreeWidgetItem(parent)
        node.setText(0, str)

    def library_lists(self):
        count = 0
        dir_list_first = os.listdir(self.path_library)
        for dir_fir in dir_list_first:
            if os.path.isdir(os.path.join(self.path_library, dir_fir)):
                # 添加第一层目录到treewidget
                self.add_node(self.media_list, dir_fir)
                dir_list_sec = os.listdir(os.path.join(self.path_library, dir_fir))
                for dir_sec in dir_list_sec:
                    if os.path.isdir(os.path.join(self.path_library, dir_fir, dir_sec)):
                        self.add_node(self.media_list.topLevelItem(count), dir_sec)
                count += 1

    def movie_lists(self):
        self.total = {}
        file_type = self.movie_type.split('|')
        file_root = self.path_movie
        for root, dirs, files in os.walk(file_root):
            for f in files:
                if os.path.splitext(f)[1] in file_type:
                    movie_info = ''
                    path = root + '/' + f
                    path = path.replace("\\\\", "/").replace("\\", "/")
                    try:
                        nfo_file = path.replace(os.path.splitext(f)[1], '.nfo')
                        file = open(nfo_file, 'rb')
                        content = file.read().decode('utf8')
                        if re.search(r'<title>(.+)</title>', content):
                            movie_info = '标题: ' + str(re.findall(r'<title>(.+)</title>', content)).strip("[',']").replace('\'', '')
                        if re.search(r'<name>(.+)</name>', content):
                            actor = str(re.findall(r'<name>(.+)</name>', content)).strip("[',']").replace('\'', '')
                            movie_info += '\n' + '演员: ' + actor
                        if re.search(r'<plot>(.+)</plot>', content):
                            outline = str(re.findall(r'<plot>(.+)</plot>', content)).strip("[',']").replace('\'', '')
                            movie_info += '\n' + '简介: ' + outline
                    except Exception as error_info:
                        print(str(error_info))
                    self.total[os.path.splitext(f)[0]] = {
                        'number': os.path.splitext(f)[0],
                        'movie': path,
                        'movie_info': movie_info,
                        'poster': path.replace(os.path.splitext(f)[1], '-poster.jpg'),
                        'thumb': path.replace(os.path.splitext(f)[1], '-thumb.jpg'),
                    }

    def resizeEvent(self, event):
        super(MyMAinWindow, self).resizeEvent(event)
        scale_w = self.Ui.centralwidget.width() / 1459
        widget_w = 200 * scale_w - 5
        widget_h = self.statusBar().y() - 10
        # 左侧
        self.Ui.widget.setGeometry(5, 5, widget_w, widget_h)
        self.Ui.gridLayoutWidget_3.setGeometry(0, 0, widget_w, widget_h)
        # 中间
        separate_w = 20 * scale_w
        self.Ui.line_separate.setGeometry(widget_w + 5, 5, separate_w, widget_h)
        # 右侧
        stackedWidget_x = widget_w + 5 + separate_w
        self.Ui.stackedWidget.setGeometry(stackedWidget_x, 5, self.Ui.centralwidget.width() - stackedWidget_x - 5, widget_h)
        self.Ui.scrollArea.setGeometry(0, 0, self.Ui.stackedWidget.width(), widget_h)


if __name__ == '__main__':
    '''
    主函数
    '''
    app = QApplication(sys.argv)
    ui = MyMAinWindow()
    ui.show()
    sys.exit(app.exec_())
