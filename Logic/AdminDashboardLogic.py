from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import *
from Logic.functions import *
from Logic.Models.Document import Document
# from PyQt5.QtCore import Qt
# from PyQt5.QtGui import QPalette
import os

relativePath = "Backend\\Files"


class AdminDashboardUserRequestLogic(QMainWindow):

    def __init__(self):
        super(AdminDashboardUserRequestLogic, self).__init__()
        loadUi('UI/AdminInterfaceUIUserRequests.ui', self)
        self.source_list = []
        self.type = "Teacher"
        self.SetButtonsLogic()
        self.FillTeacherTable()

    def FillTeacherTable(self):
        self.type = "Teacher"
        self.source_list = []
        self.source_list = functions.getTeachersStatus(0)
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem("Name")
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem("Designation")
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem("Email")
        self.tableWidget.setHorizontalHeaderItem(3, item)
        if self.source_list is not None:
            self.tableWidget.setColumnWidth(0, 100)
            self.tableWidget.setColumnWidth(1, 100)
            self.tableWidget.setRowCount(len(self.source_list))

            for i in range(0, len(self.source_list)):

                chkBoxItem = QTableWidgetItem()
                chkBoxItem.setFlags(
                    QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
                chkBoxItem.setCheckState(QtCore.Qt.Unchecked)
                self.tableWidget.setItem(i, 0, chkBoxItem)

                self.tableWidget.setItem(
                    i, 1, QTableWidgetItem(str(self.source_list[i][0])))
                self.tableWidget.setItem(
                    i, 2, QTableWidgetItem(str(self.source_list[i][1])))
                self.tableWidget.setItem(
                    i, 3, QTableWidgetItem(str(self.source_list[i][2])))

    def FillStudentTable(self):
        self.type = "Student"
        self.source_list = []
        self.source_list = functions.getStudentStatus(0)
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem("Registration No")
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem("Name")
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem("Email")
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem("Session")
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem("Section")
        self.tableWidget.setHorizontalHeaderItem(5, item)

        if self.source_list is not None:
            self.tableWidget.setColumnWidth(0, 100)
            self.tableWidget.setColumnWidth(1, 100)
            self.tableWidget.setRowCount(len(self.source_list))

            for i in range(0, len(self.source_list)):
                chkBoxItem = QTableWidgetItem()
                chkBoxItem.setFlags(
                    QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
                chkBoxItem.setCheckState(QtCore.Qt.Unchecked)
                self.tableWidget.setItem(i, 0, chkBoxItem)

                self.tableWidget.setItem(
                    i, 1, QTableWidgetItem(str(self.source_list[i][0])))
                self.tableWidget.setItem(
                    i, 2, QTableWidgetItem(str(self.source_list[i][1])))
                self.tableWidget.setItem(
                    i, 3, QTableWidgetItem(str(self.source_list[i][2])))
                self.tableWidget.setItem(
                    i, 4, QTableWidgetItem(str(self.source_list[i][3])))
                self.tableWidget.setItem(
                    i, 5, QTableWidgetItem(str(self.source_list[i][4])))

    def SetButtonsLogic(self):
        self.menu_btn_upload_document.clicked.connect(
            self.UploadDocumentButtonClicked)
        self.teachersViewBtn.clicked.connect(self.FillTeacherTable)
        self.studentsViewBtn.clicked.connect(self.FillStudentTable)
        self.ApproveBtn.clicked.connect(self.ApproveButtonClicked)

    def ApproveButtonClicked(self):
        if self.type == "Teacher":
            self.source_list = functions.getTeachersStatus(0)
            for i in range(self.tableWidget.rowCount()):
                if self.tableWidget.item(i, 0).checkState() == QtCore.Qt.Checked:
                    teacherId = functions.GetTeacherId(
                        self.tableWidget.item(i, 3).text())
                    functions.approvedTeacher(
                        1, teacherId[0][0])
            self.FillTeacherTable()
        elif self.type == "Student":
            self.source_list = functions.getStudentStatus(0)
            for i in range(self.tableWidget.rowCount()):
                if self.tableWidget.item(i, 0).checkState() == QtCore.Qt.Checked:
                    functions.approvedStudent(1, self.source_list[i][0])
            self.FillStudentTable()

    def UploadDocumentButtonClicked(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = AdminDashboardUploadDocumentLogic()
        self.ui.show()
        self.close()


class AdminDashboardUploadDocumentLogic(QMainWindow):
    def __init__(self):
        super(AdminDashboardUploadDocumentLogic, self).__init__()
        loadUi('UI/AdminInterfaceUIUploadDocument.ui', self)
        self.file_path = ""
        self.SetButtonsLogic()
        self.PopulateDataInLists()

    def PopulateDataInLists(self):
        self.GetTeachersList()
        self.GetStudentsList()
        self.GetSessionsList()

    def GetTeachersList(self):
        data = functions.getTeachersStatus(1)
        for i in range(len(data)):
            list_item = QListWidgetItem()
            checkbox = QCheckBox()
            checkbox.setText(data[i][0])
            list_item.setSizeHint(checkbox.sizeHint())
            self.TeachersList.addItem(list_item)
            self.TeachersList.setItemWidget(list_item, checkbox)

    def GetStudentsList(self):
        data = functions.getStudentStatus(1)
        print(data)
        for i in range(len(data)):
            list_item = QListWidgetItem()
            checkbox = QCheckBox()
            checkbox.setText(data[i][0])
            list_item.setSizeHint(checkbox.sizeHint())
            self.StudentsList.addItem(list_item)
            self.StudentsList.setItemWidget(list_item, checkbox)

    def GetSessionsList(self):
        data = functions.getStudentSession()
        for i in range(len(data)):
            list_item = QListWidgetItem()
            checkbox = QCheckBox()
            checkbox.setText(data[i][0])
            list_item.setSizeHint(checkbox.sizeHint())
            self.SessionsList.addItem(list_item)
            self.SessionsList.setItemWidget(list_item, checkbox)

    def SetButtonsLogic(self):
        self.menu_btn_users_request.clicked.connect(
            self.UserRequestButtonClicked)
        self.uploadFileBtn.clicked.connect(self.open_file_dialog)
        self.teachersToggle.clicked.connect(self.TeachersToggleClicked)
        self.studentsToggle.clicked.connect(self.StudentsToggleClicked)
        self.sessionToggle.clicked.connect(self.SessionsToggleClicked)
        self.SubmitBtn.clicked.connect(self.SubmitButtonClicked)

    def TeachersToggleClicked(self):
        total_items = self.TeachersList.count()
        checked_items = sum(self.TeachersList.itemWidget(
            self.TeachersList.item(index)).isChecked() for index in range(total_items))

        if checked_items <= 1:
            # Check all items
            for index in range(total_items):
                item = self.TeachersList.item(index)
                checkbox = self.TeachersList.itemWidget(item)
                checkbox.setChecked(True)
        elif checked_items == total_items:
            # Uncheck all items
            for index in range(total_items):
                item = self.TeachersList.item(index)
                checkbox = self.TeachersList.itemWidget(item)
                checkbox.setChecked(False)

    def StudentsToggleClicked(self):
        total_items = self.StudentsList.count()
        checked_items = sum(self.StudentsList.itemWidget(
            self.StudentsList.item(index)).isChecked() for index in range(total_items))

        if checked_items <= 1:
            # Check all items
            for index in range(total_items):
                item = self.StudentsList.item(index)
                checkbox = self.StudentsList.itemWidget(item)
                checkbox.setChecked(True)
        elif checked_items == total_items:
            # Uncheck all items
            for index in range(total_items):
                item = self.StudentsList.item(index)
                checkbox = self.StudentsList.itemWidget(item)
                checkbox.setChecked(False)

    def SessionsToggleClicked(self):
        total_items = self.SessionsList.count()
        checked_items = sum(self.SessionsList.itemWidget(
            self.SessionsList.item(index)).isChecked() for index in range(total_items))

        if checked_items <= 1:
            # Check all items
            for index in range(total_items):
                item = self.SessionsList.item(index)
                checkbox = self.SessionsList.itemWidget(item)
                checkbox.setChecked(True)
        if checked_items == total_items:
            # Uncheck all items
            for index in range(total_items):
                item = self.SessionsList.item(index)
                checkbox = self.SessionsList.itemWidget(item)
                checkbox.setChecked(False)

    def open_file_dialog(self):
        file_dialog = QFileDialog()
        self.file_path, _ = file_dialog.getOpenFileName(self, "Select File")

        if self.file_path:
            print("Selected file:", self.file_path)

    def UserRequestButtonClicked(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = AdminDashboardUserRequestLogic()
        self.ui.show()
        self.close()

    def retrieve_checked_items(self, type, list_widget):
        checked_items = []

        for index in range(list_widget.count()):
            item = list_widget.item(index)
            checkbox = list_widget.itemWidget(item)
            if checkbox.checkState() == 2:  # 2 represents checked state
                checked_items.append(f"{type}.{checkbox.text()}")
        return checked_items

    def SubmitButtonClicked(self):
        teachersTag = self.retrieve_checked_items("Teacher", self.TeachersList)
        studentsTag = self.retrieve_checked_items("Student", self.StudentsList)
        sessionsTag = self.retrieve_checked_items("Student", self.SessionsList)
        if self.file_path:
            tags = ",".join(studentsTag + teachersTag + sessionsTag)
            tagList = tags.split(",")
            path = relativePath + "\\" + os.path.basename(self.file_path)
            if path != "":
                doc = Document(path, tagList, self.file_path)
                functions.createDocument(doc)
