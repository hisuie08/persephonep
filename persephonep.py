#!/usr/bin/env python
# coding: utf-8
#

import sys
from PyQt5.QtWidgets import QMainWindow, QWidget, QPushButton, QTabWidget, QApplication, QHBoxLayout, QVBoxLayout, QLabel, QGridLayout
from PyQt5.QtGui import QIcon
from func_persephonep import *
from PyQt5.QtCore import pyqtSlot

__program__ = 'PERSEPHONEP'

class PersephoneMainWidget(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = __program__
        self.left = 100
        self.top = 100
        self.width = 1200
        self.height = 800
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.table_widget = PersephoneTableWidget(self)
        self.setCentralWidget(self.table_widget)

        self.show()

class PersephoneTableWidget(QWidget):

    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.layout = QVBoxLayout(self)

        
        # initialize tab screen
        self.tabs = QTabWidget()
        # self.tab1 = QWidget()
        # self.tab2 = QWidget()
        self.tab = []
        self.tabs.resize(1200, 800)

        # Add Tabs
        self._addTab(0)
        # self.tabs.addTab(self.tab1, 'Tab 1')
        # self.tabs.addTab(self.tab2, 'Tab 2')
        self.add_button = QPushButton('+')
        self.add_button.setStyleSheet('background-color:gray')
        self.add_button.clicked.connect(self._addTab)
        self.app_info = QLabel('PERSEPHONE is a Web Browser based on Python 3 and PyQt5, developed by @montblanc18.')

        # define the delete tab process
        self.tabs.tabCloseRequested.connect(self.closeTab)
        

        #
        self.tabs.setTabsClosable(True)
        self.tabs.setUsesScrollButtons(True)
        ########## Create first tab
        #self.tab[0].layout = QVBoxLayout(self)
        #self.pushButton1 = QPushButton('PyQt5 button')
        #self.tab[0].layout.addWidget(self.pushButton1)
        #self.tab[0].setLayout(self.tab[0].layout)

        # Add tabs to widget
        self.layout.addWidget(self.add_button)
        self.layout.addWidget(self.tabs)
        self.layout.addWidget(self.app_info)
        self.setLayout(self.layout)

    def _addTab(self, index):
        ''' add Tab
        '''
        self.tab.append(PersephoneWindow(parent = self))
        self.tabs.addTab(self.tab[index-1], '')

    def closeTab(self, index):
        ''' close Tab. 
        '''
        widget = self.tabs.widget(index)
        self.tabs.removeTab(index)
        
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
            print(currentQTableWidgetItem.row(), currentQTableWidgetItem.column(), currentQTableWidgetItem.text())

    
if __name__ == '__main__':
    app = QApplication(sys.argv)

    # setWindowIcon is a method for QApplication, not for QWidget
    path = os.path.join(os.path.dirname(sys.modules[__name__].__file__), 'icon_persephone.png')
    app.setWindowIcon(QIcon(path))

    
    ui = PersephoneMainWidget()
    sys.exit(app.exec_())
