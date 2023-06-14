from PyQt5 import QtCore, QtGui, QtWidgets
from Logic.TeacherStudentDashboardScreenLogic import UserDashboardScreenLogic
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import *
from Logic.Utilities.validations import Validations
from Logic.functions import functions


class TeacherRegistrationScreenLogic(QMainWindow):
    def __init__(self):
        super(TeacherRegistrationScreenLogic, self).__init__()
        loadUi('UI/TeacherRegistration.ui', self)
        self.SetButtonsLogic()

    def SetButtonsLogic(self):
        self.registerBtn.clicked.connect(self.RegisterButtonClicked)

    def RegisterButtonClicked(self):
        name = self.nametxt.text()
        email = self.emailtxt.text()
        password = self.passwordtxt.text()
        designation = self.designationtxt.text()
        isValid = self.validateTeacherInput()
        if (isValid):
            isCreated = functions.createTeacher(
                name, designation, email, password)
            if (isCreated):
                msg = QMessageBox()
                msg.setWindowTitle("Success")
                msg.setText(
                    "Teacher Registered Successfully! Wait for your Account Approval")
                msg.setIcon(QMessageBox.Information)
                msg.exec_()
                self.window = QtWidgets.QMainWindow()
                self.ui = UserDashboardScreenLogic()
                self.ui.show()
                self.close()
            else:
                msg = QMessageBox()
                msg.setWindowTitle("Error")
                msg.setText("Teacher Registration Failed! Try Again Later")
                msg.setIcon(QMessageBox.Critical)
                msg.exec_()

    def validateTeacherInput(self):
        name = self.nametxt.text()
        email = self.emailtxt.text()
        password = self.passwordtxt.text()
        designation = self.designationtxt.text()
        return (Validations.NameValidation(name) and Validations.EmailValidation(email) and Validations.PasswordValidation(password))
