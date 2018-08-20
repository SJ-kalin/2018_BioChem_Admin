import sys
import os
from PyQt5.QtWidgets import (QWidget, QPushButton,
                             QHBoxLayout, QVBoxLayout, QApplication)
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem, QFileDialog
from PyQt5.QtCore import pyqtSlot
import excel_loader


class Main_Activity(QWidget):
    listArr = []

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
        add_button = QPushButton("ADD", self)
        delete_button = QPushButton("DEL", self)
        add_button.setStyleSheet("background-color: #d9534f")
        delete_button.setStyleSheet("background-color: #428bca")
        delete_button.clicked.connect(self.delete_list)
        add_button.clicked.connect(self.openFileNamesDialog)

        second_box.addStretch(1)
        second_box.addWidget(add_button)
        second_box.addWidget(delete_button)

        third_box = QVBoxLayout()
        push_button = QPushButton("hello")
        push_button.setStyleSheet("background-color: #5cb85c")
        third_box.addWidget(push_button)
        push_button.clicked.connect(self.saveFileDialog)

        # box들을 메인 뷰에 추가한다.
        main.addLayout(first_box)
        main.addLayout(second_box)
        main.addLayout(third_box)
        self.setLayout(main)

        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle('바이오 융합 - 설문조사 병합')
        self.show()

    @pyqtSlot()
    def delete_list(self):

        items = self.tableWidget.selectedItems()
        indexes = self.tableWidget.selectionModel().selectedRows()

        # 한번에 전부 다 지울경우
        if indexes.__len__() is self.listArr.__len__():
            self.listArr.clear()
            self.tableWidget.setColumnCount(0)
            self.tableWidget.setRowCount(0)
            return

        print("items : ", items)
        print("array: ", self.listArr)

        for item in items:
            self.listArr.remove(item.text())

        self.tableWidget.setColumnCount(1)
        self.tableWidget.setRowCount(self.listArr.__len__())
        for num, key in zip(range(0, self.listArr.__len__()), self.listArr):
            self.tableWidget.setItem(num, 0, QTableWidgetItem(key))

        self.tableWidget.setHorizontalHeaderLabels(("File name ",))
        self.tableWidget.horizontalHeader().setStretchLastSection(True)

    # Create table
    def createTable(self):
        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(self.listArr.__len__())
        self.tableWidget.setColumnCount(1)

        for num, key in zip(range(0, self.listArr.__len__()), self.listArr):
            self.tableWidget.setItem(num, 0, QTableWidgetItem(key))

        # self.tableWidget.setItem(0, 0, QTableWidgetItem("Cell (1,1)"))

        self.tableWidget.setHorizontalHeaderLabels(("File name ",))
        self.tableWidget.move(0, 0)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)

    def openFileNamesDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        files, _ = QFileDialog.getOpenFileNames(self, "병합할 엑셀 파일을 선택합니다.", "",
                                                "All Files (*);;엑셀 파일 (*.xlsx)", options=options)

        if self.tableWidget.columnCount() != 1:
            self.tableWidget.setColumnCount(1)

        for file in files:
            # file_name = file.split(os.sep)[-1:]
            # file_name = str(file_name)
            # self.tableWidget.rowCount()
            self.listArr.append(file)
            self.tableWidget.setRowCount(self.tableWidget.rowCount() + 1)
            self.tableWidget.setItem(self.tableWidget.rowCount() - 1, 0, QTableWidgetItem(file))
            self.tableWidget.reset()

    def get_excel_files(self, file_name):
        excel_loader.getExcelFile(self.listArr, file_name)

    # 저장할 파일명을 절대경로 형식으로 리턴한ㄷ.
    def saveFileDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getSaveFileName(self, "QFileDialog.getSaveFileName()", "",
                                                  "All Files (*);;Text Files (*.txt)", options=options)
        if fileName:
            print(fileName)
        self.get_excel_files(fileName)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Main_Activity()
    ex.setMinimumSize(500, 500)
    ex.setMaximumSize(800, 800)
    sys.exit(app.exec_())
