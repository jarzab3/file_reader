#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
__author__ = "Adam Jarzebak"
__copyright__ = "Copyright 2018, Adam Jarzebak"
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = "Adam Jarzebak"
__email__ = "adam@jarzebak.eu"
__status__ = "Testing"
"""
import sys
from PyQt5.QtWidgets import QWidget, QMessageBox, QApplication
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QAction, QTableWidget,QTableWidgetItem,QVBoxLayout
from PyQt5.QtCore import pyqtSlot

class FileReader(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()


    def get_current_window_info(self) -> None:
        """
        Getting information about current screen. Returns information such as: screen height and screen width.
        :return: screen details: width, height: list
        """
        screen = app.primaryScreen()
        #print('Screen: %s' % screen.name())
        size = screen.size()
        #print('Size: %d x %d' % (size.width(), size.height()))
        rect = screen.availableGeometry()
        #print('Available: %d x %d' % (rect.width(), rect.height()))
        return [rect.width(), rect.height()]

    def initUI(self) -> None:
        """
        Initialization of window. Function will set up approx. 70% of window size.
        """
        ratio = 70
        width_to_set = (ratio * self.get_current_window_info()[0]) / 100.0
        height_to_set = (ratio * self.get_current_window_info()[1]) / 100.0
        self.setGeometry(200, 100, width_to_set, height_to_set)
        self.createTable()
        # Add box layout, add table to box layout and add box layout to widget
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.tableWidget)
        self.setLayout(self.layout)
        self.setWindowTitle('View files')
        self.show()

    def createTable(self):
       # Create table
        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(4)
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setItem(0,0, QTableWidgetItem("Cell (1,1)"))
        self.tableWidget.setItem(0,1, QTableWidgetItem("Cell (1,2)"))
        self.tableWidget.setItem(1,0, QTableWidgetItem("Cell (2,1)"))
        self.tableWidget.setItem(1,1, QTableWidgetItem("Cell (2,2)"))
        self.tableWidget.setItem(2,0, QTableWidgetItem("Cell (3,1)"))
        self.tableWidget.setItem(2,1, QTableWidgetItem("Cell (3,2)"))
        self.tableWidget.setItem(3,0, QTableWidgetItem("Cell (4,1)"))
        self.tableWidget.setItem(3,1, QTableWidgetItem("Cell (4,2)"))
        self.tableWidget.move(0,0)

        # table selection change
        self.tableWidget.doubleClicked.connect(self.on_click)


    @pyqtSlot()
    def on_click(self):
        print("\n")
        for currentQTableWidgetItem in self.tableWidget.selectedItems():
            print(currentQTableWidgetItem.row(), currentQTableWidgetItem.column(), currentQTableWidgetItem.text())


    def create_table_view(self):
        self.tableWidget = QTableWidget()
        # set row count
        self.tableWidget.setRowCount(4)
        # set column count
        self.tableWidget.setColumnCount(2)

    def closeEvent(self, event) -> None:
        reply = QMessageBox.question(self, 'Message',
            "Are you sure to quit?", QMessageBox.Yes |
            QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = FileReader()
    ex.create_table_view()
    #ex.get_current_window_info()
    sys.exit(app.exec_())


