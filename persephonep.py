#!/usr/bin/env python
# coding: utf-8
#

import sys
import os
from PyQt5.QtWidgets import (QMainWindow, QWidget, QPushButton,
                             QTabWidget, QApplication,
                             # QHBoxLayout, QGridLayout,
                             QVBoxLayout, QLabel, QDesktopWidget)
from PyQt5.QtGui import QIcon
# from func_persephonep import *
from func_persephonep import PersephonepWindow
from PyQt5.QtCore import pyqtSlot

__program__ = 'PERSEPHONEP'

''' This is a main window of the browser.
    This class includes PersephonepMainWidget.
'''


class PersephonepMainWidget(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = __program__
        self.left = 100
        self.top = 100
        self.width = 1200
        self.height = 800
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.table_widget = PersephonepTableWidget(self)
        self.setCentralWidget(self.table_widget)

        self.show()


''' This is a Tab Handle Class for this browser.
    This class is called by PersephonepMainWindow,
    and it has some PersephonepWindos.
'''


class PersephonepTableWidget(QWidget):

    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.layout = QVBoxLayout(self)

        # initialize tab screen
        self.tabs = QTabWidget()
        #  self.tab1 = QWidget()
        #  self.tab2 = QWidget()
        self.tab = []  # Store the PersephonepWindow Class
        self.tabs.resize(1200, 800)

        # Add Tabs
        self._addTab(len(self.tab))  # len(self.tab) => 0
        # self.tabs.addTab(self.tab1, 'Tab 1')
        # self.tabs.addTab(self.tab2, 'Tab 2')
        self.add_button = QPushButton('+')
        self.add_button.setStyleSheet('background-color:gray')
        # add tab to last of index
        self.add_button.clicked.connect(lambda: self._addTab(len(self.tab)))
        app_info_text = '%s is a Web Browser based on Python 3 and PyQt5,' \
                        ' developed by @montblanc18.' % __program__
        self.app_info = QLabel(app_info_text)

        # define the delete tab process
        self.tabs.setTabsClosable(True)
        self.tabs.tabCloseRequested.connect(self.closeTab)

        self.tabs.setUsesScrollButtons(True)
        # Create first tab
        # self.tab[0].layout = QVBoxLayout(self)
        # self.pushButton1 = QPushButton('PyQt5 button')
        # self.tab[0].layout.addWidget(self.pushButton1)
        # self.tab[0].setLayout(self.tab[0].layout)

        # Add tabs to widget
        self.layout.addWidget(self.add_button)
        self.layout.addWidget(self.tabs)
        self.layout.addWidget(self.app_info)
        self.setLayout(self.layout)

    def _addTab(self, index):
        ''' add Tab
        '''
        self.tab.append(PersephonepWindow(parent=self))
        #  do not match tab index & tab num
        self.tabs.addTab(self.tab[-1], '')
        self.tabs.setTabText(index, 'VanilaPage')
        self.tab[-1].window.titleChanged.connect(self.updateTabName)

    def closeTab(self, index):
        ''' close Tab.
        '''
        # widget = self.tabs.widget(index)
        self.tab.pop(index)
        self.tabs.removeTab(index)

    def updateTabName(self):
        ''' re-set tab name
        '''
        self.tabs.setTabText(self.tabs.currentIndex(),
                             self.tab[self.tabs.currentIndex()].window.title())

    def center(self):
        ''' centering widget
        '''
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    @pyqtSlot()
    def on_click(self):
        print("\n")
        for currentQTableWidgetItem in self.tableWidget.selectedItems():
            print(currentQTableWidgetItem.row(),
                  currentQTableWidgetItem.column(),
                  currentQTableWidgetItem.text())


if __name__ == '__main__':
    app = QApplication(sys.argv)

    # setWindowIcon is a method for QApplication, not for QWidget
    path = os.path.join(os.path.dirname(sys.modules[__name__].__file__),
                        'icon_persephone.png')
    app.setWindowIcon(QIcon(path))

    # app.setApplicationName('IE')
    # app.setApplicationVersion('1.0')

    ui = PersephonepMainWidget()
    sys.exit(app.exec_())
