from PyQt5 import QtCore, QtGui, QtWidgets
from Logic.StuRegistrationScreenLogic import StuRegistrationScreenLogic
from Logic.TeacherRegistrationScreenLogic import TeacherRegistrationScreenLogic

from PyQt5.uic import loadUi
from PyQt5.QtWidgets import *


class RegisterOptionScreenLogic(QMainWindow):
    def __init__(self):
        super(RegisterOptionScreenLogic, self).__init__()
        loadUi('UI/registerOption.ui', self)
        self.SetButtonsLogic()

    def SetButtonsLogic(self):
        self.loginBtn.clicked.connect(self.RegisterStudentButtonClicked)
        self.loginBtn_2.clicked.connect(self.RegisterTeacherButtonClicked)

    def RegisterStudentButtonClicked(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = StuRegistrationScreenLogic()
        self.ui.show()
        self.close()

    def RegisterTeacherButtonClicked(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = TeacherRegistrationScreenLogic()
        self.ui.show()
        self.close()
