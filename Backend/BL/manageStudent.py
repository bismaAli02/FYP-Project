from Backend.BL.Models.Student import Student
from Backend.DAL.AccountInfoDAL import AccountInfoDAL
from Backend.DAL.StudentDAL import studentDAL
from Backend.BL.Services.encryption import encryption
from Backend.Logs.logger import Logger
import logging


class manageStudent:
    def createStudentAccount(self, student: Student):
        try:
            encryptedPassword = encryption.encryptedPassword(
                student.getAccountInfo()['password'])
            student.setPassword(encryptedPassword)
            account = AccountInfoDAL.getInstance()
            accId = account.createAccount(student)
            if (accId is not None):
                std = studentDAL.getInstance()
                std.createStudentAccount(student, accId)
        except Exception as e:
            msg = "Error in Manage Student's Create Student Account Function: " + \
                str(e)
            Logger.CreateLog(
                logging.ERROR, msg)
            pass

    def updateStudentStatus(self, status, registrationNumber):
        try:
            std = studentDAL.getInstance()
            std.updateStudentStatus(status, registrationNumber)
        except Exception as e:
            msg = "Exception in manage student's update student status Function: " + \
                str(e)
            Logger.CreateLog(
                logging.ERROR, msg)
            pass

    def getStudents(self, status):
        try:
            std = studentDAL.getInstance()
            results = std.getStudents(status)
        except Exception as e:
            results = []
            msg = "Exception in manage student's get student function: " + \
                str(e)
            Logger.CreateLog(
                logging.ERROR, msg)
            pass
        finally:
            return results
    
    def getStudentSession(self):
        try:
            std = studentDAL.getInstance()
            results = std.getStudentSession()
        except Exception as e:
            results = []
            msg = "Exception in manage student's get student Session function: " + \
                str(e)
            Logger.CreateLog(
                logging.ERROR, msg)
            pass
        finally:
            return results
