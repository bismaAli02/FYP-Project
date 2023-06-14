import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from Logic.LoginScreen import LoginScreenLogic
from Logic.AdminDashboardLogic import *
import appdirs
import json
import os

# print(appdirs.user_data_dir(appname="app"))


app = QtWidgets.QApplication(sys.argv)
ui = LoginScreenLogic()
ui.show()
sys.exit(app.exec_())
