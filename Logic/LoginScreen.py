from PyQt5 import QtCore, QtGui, QtWidgets
from Logic.RegisterOptionScreen import RegisterOptionScreenLogic
from Logic.AdminDashboardLogic import AdminDashboardUserRequestLogic
from Logic.TeacherStudentDashboardScreenLogic import UserDashboardScreenLogic
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import *

from Backend.BL.manageStudent import manageStudent
from Backend.BL.manageTeacher import manageTeacher
from Backend.BL.manageDocument import manageDocument
from Backend.BL.Services.login import loginServices
from Backend.Logs.logger import Logger
import logging
from Logic.Utilities.validations import Validations
from Logic.functions import *


class LoginScreenLogic(QMainWindow):
    def __init__(self):
        super(LoginScreenLogic, self).__init__()
        loadUi('UI/login.ui', self)
        self.SetButtonsLogic()

    def SetButtonsLogic(self):
        self.RegisterBtn.clicked.connect(self.RegisterBtnClicked)
        self.loginBtn.clicked.connect(self.LoginBtnClicked)

    def RegisterBtnClicked(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = RegisterOptionScreenLogic()
        self.ui.show()
        self.close()

    def LoginBtnClicked(self):
        email = self.UserNametxt.text()
        isEmailCorrect = Validations.EmailValidation(email)
        password = self.Passwordtxt.text()
        isPasswordCorrect = Validations.PasswordValidation(password)
        if (isEmailCorrect and isPasswordCorrect):
            if (email == "admin@admin.com" and password == "admin@123"):
                self.window = QtWidgets.QMainWindow()
                self.ui = AdminDashboardUserRequestLogic()
                self.ui.show()
                self.close()
            else:
                documents, x, userId = functions.userLoggin(
                    email, password, "Student")
                print(userId)
                if (x):
                    self.window = QtWidgets.QMainWindow()
                    self.ui = UserDashboardScreenLogic(documents, userId)
                    self.ui.show()
                    self.close()
                    return
                documents, y, userId = functions.userLoggin(
                    email, password, "Teacher")
                if (y):
                    self.window = QtWidgets.QMainWindow()
                    self.ui = UserDashboardScreenLogic(documents, userId)
                    self.ui.show()
                    self.close()
