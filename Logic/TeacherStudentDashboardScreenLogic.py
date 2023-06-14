from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import *
from Logic.Models.Document import Document
import os
import requests
import shutil
from Logic.functions import *


class UserDashboardScreenLogic(QMainWindow):
    def __init__(self, documents: Document, userId):
        super(UserDashboardScreenLogic, self).__init__()
        loadUi('UI/TeacherStudentUIDashboard.ui', self)
        self.documents = documents
        self.UserId = userId
        self.SetButtonsLogic()
        self.PopulateDataInTable()

    def SetButtonsLogic(self):
        self.downloadBtn.clicked.connect(self.DownloadBtnClicked)

    def DownloadBtnClicked(self):
        for i in range(self.documentsTable.rowCount()):
            if self.documentsTable.item(i, 0).checkState() == QtCore.Qt.Checked:
                print(self.documentsTable.item(i, 0).text())
                print(self.documentsTable.item(i, 1).text())
                for item in self.documents:
                    if item[0] == self.documentsTable.item(i, 1).text():
                        isFileDownloaded = self.download_file(
                            self.documentsTable.item(i, 1).text())
                        functions.UpdateDocumentStatus(
                            int(self.UserId), int(item[1]))
                        print(self.UserId)
                        print(item[1])
                # print(self.documentsTable.item(i, 2).text())
                # teacherId = functions.GetTeacherId(
                #     self.documentsTable.item(i, 3).text())
                # functions.approvedTeacher(
                #     1, teacherId[0][0])
        self.PopulateDataInTable()

    def PopulateDataInTable(self):
        self.documentsTable.setColumnCount(2)
        self.documentsTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.documentsTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem("Path")
        self.documentsTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem("Id")
        self.documentsTable.setHorizontalHeaderItem(2, item)
        if self.documents is not None:
            self.documentsTable.setColumnWidth(0, 100)
            self.documentsTable.setColumnWidth(1, 100)
            self.documentsTable.setRowCount(len(self.documents))

            for i in range(0, len(self.documents)):

                chkBoxItem = QTableWidgetItem()
                chkBoxItem.setFlags(
                    QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
                chkBoxItem.setCheckState(QtCore.Qt.Unchecked)
                self.documentsTable.setItem(i, 0, chkBoxItem)

                self.documentsTable.setItem(
                    i, 1, QTableWidgetItem(str(self.documents[i][0])))
                self.documentsTable.setItem(
                    i, 2, QTableWidgetItem(str(self.documents[i][1])))

    def select_folder(self):
        self.folder_path = QFileDialog.getExistingDirectory(
            self, "Select Folder")
        print("Folder path:", self.folder_path)

    def download_file(self, file_url):
        self.select_folder()
        if not self.folder_path:
            # self.download_file(file_url)
            return

        currentDir = os.getcwd()
        file_url = os.path.join(currentDir, file_url)
        print(file_url)

        try:
            if file_url.startswith(('http://', 'https://')):
                response = requests.get(file_url, stream=True)
                if response.status_code == 200:
                    file_name = os.path.basename(file_url)
                    file_path = os.path.join(self.folder_path, file_name)

                    with open(file_path, "wb") as file:
                        for chunk in response.iter_content(chunk_size=1024):
                            file.write(chunk)

                    print("File downloaded successfully.")
                    return True
                else:
                    print("Failed to download file:", response.status_code)
                    return False
            else:
                file_name = os.path.basename(file_url)
                destination_path = os.path.join(self.folder_path, file_name)

                shutil.copy(file_url, destination_path)
                print("File copied successfully.")
                return True
        except Exception as e:
            print("Error occurred while downloading or copying file:", str(e))
            return False
