from PyQt5 import QtCore, QtGui, QtWidgets
from Logic.TeacherStudentDashboardScreenLogic import UserDashboardScreenLogic
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import *
from Logic.Utilities.validations import Validations
from Logic.functions import functions


class StuRegistrationScreenLogic(QMainWindow):
    def __init__(self):
        super(StuRegistrationScreenLogic, self).__init__()
        loadUi('UI/StuRegistration.ui', self)
        self.SetButtonsLogic()

    def SetButtonsLogic(self):
        self.registerBtn.clicked.connect(self.RegisterButtonClicked)

    def RegisterButtonClicked(self):
        name = self.Nametxt.text()
        reg = self.regtxt.text()
        email = self.emailtxt.text()
        password = self.passwordtxt.text()
        section = self.sectiontxt.text()
        session = self.sessiontxt.text()
        isValid = self.validateStudentInput()
        if (isValid):
            isCreated = functions.creatStudent(
                name, reg, email, password, section, session)
            if (isCreated):
                msg = QMessageBox()
                msg.setWindowTitle("Success")
                msg.setText(
                    "Student Registered Successfully! Wait for your Account Approval")
                msg.setIcon(QMessageBox.Information)
                msg.exec_()
                self.window = QtWidgets.QMainWindow()
                self.ui = UserDashboardScreenLogic()
                self.ui.show()
                self.close()
            else:
                msg = QMessageBox()
                msg.setWindowTitle("Error")
                msg.setText("Student Registration Failed! Try Again Later")
                msg.setIcon(QMessageBox.Critical)
                msg.exec_()

        # self.window = QtWidgets.QMainWindow()
        # self.ui = UserDashboardScreenLogic()
        # self.ui.show()
        # self.close()

    def validateStudentInput(self):
        name = self.Nametxt.text()
        reg = self.regtxt.text()
        email = self.emailtxt.text()
        password = self.passwordtxt.text()
        section = self.sectiontxt.text()
        session = self.sessiontxt.text()
        return (Validations.NameValidation(name) and Validations.RegisterNoValidations(reg) and Validations.EmailValidation(email) and Validations.PasswordValidation(password) and Validations.SectionValidation(section) and Validations.SessionValidation(session, reg))
