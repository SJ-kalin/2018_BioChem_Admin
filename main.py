import sys
from os import times_result

from PyQt5.QtWidgets import (QWidget, QPushButton,
                             QHBoxLayout, QVBoxLayout, QApplication)
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem
from PyQt5.QtCore import pyqtSlot


class Main_Activity(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        main = QVBoxLayout()

        # 첫 번째 박스에
        first_box = QVBoxLayout()
        self.createTable()
        first_box.addWidget(self.tableWidget)

        second_box = QHBoxLayout()
        add_button = QPushButton("ADD")
        delete_button = QPushButton("DEL", self)
        add_button.setStyleSheet("background-color: #d9534f")
        delete_button.setStyleSheet("background-color: #428bca")
        delete_button.clicked.connect(self.print_index)

        second_box.addStretch(1)
        second_box.addWidget(add_button)
        second_box.addWidget(delete_button)

        third_box = QVBoxLayout()
        push_button = QPushButton("hello")
        push_button.setStyleSheet("background-color: #5cb85c")
        third_box.addWidget(push_button)

        # box들을 메인 뷰에 추가한다.
        main.addLayout(first_box)
        main.addLayout(second_box)
        main.addLayout(third_box)
        self.setLayout(main)

        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle('Buttons')
        self.show()

    @pyqtSlot()
    def print_index(self):
        indexes = self.tableWidget.selectionModel().selectedRows()
        for index in sorted(indexes):
            print('Row %d is selected' % index.row())

    # Create table
    def createTable(self):
        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(4)
        self.tableWidget.setColumnCount(1)
        self.tableWidget.setItem(0, 0, QTableWidgetItem("Cell (1,1)"))
        self.tableWidget.setItem(1, 0, QTableWidgetItem("Cell (2,1)"))
        self.tableWidget.setItem(2, 0, QTableWidgetItem("Cell (3,1)"))
        self.tableWidget.setItem(3, 0, QTableWidgetItem("Cell (4,1)"))
        self.tableWidget.setHorizontalHeaderLabels(("File name ",))
        self.tableWidget.move(0, 0)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Main_Activity()
    ex.setMinimumSize(500, 500)
    ex.setMaximumSize(800, 800)
    sys.exit(app.exec_())
