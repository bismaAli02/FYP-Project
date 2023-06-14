from Backend.BL.Models.Teacher import Teacher
from Backend.DAL.AccountInfoDAL import AccountInfoDAL
from Backend.DAL.TeacherDAL import TeacherDAL
from Backend.BL.Services.encryption import encryption
from Backend.Logs.logger import Logger
import logging


class manageTeacher:
    def createTeacher(self, teacher: Teacher):
        try:
            encryptedPassword = encryption.encryptedPassword(
                teacher.getAccountInfo()['password'])
            teacher.setPassword(encryptedPassword)
            account = AccountInfoDAL.getInstance()
            accId = account.createAccount(teacher)
            if (accId is not None):
                teach = TeacherDAL.getInstance()
                teach.createTeacher(teacher, accId)
        except Exception as e:
            msg = "Error in Manage Teacher's Create Teacher Function: " + \
                str(e)
            Logger.CreateLog(
                logging.ERROR, msg)
            pass

    def updateTeacherStatus(self, status, teacherId):
        try:
            teach = TeacherDAL.getInstance()
            teach.updateTeacherStatus(status, teacherId)
        except Exception as e:
            msg = "Exception in manage teacher's update teacher status function: " + \
                str(e)
            Logger.CreateLog(
                logging.ERROR, msg)
            pass

    def GetTeacherById(self, email):
        try:
            teach = TeacherDAL.getInstance()
            result = teach.getTeacherId(email)
        except Exception as e:
            result = 0
            msg = "error in manage teacher's Get Teacher Id function: " + \
                str(e)
            Logger.CreateLog(
                logging.ERROR, msg)
            pass
        finally:
            return result

    def getTeachers(self, status):
        try:
            teach = TeacherDAL.getInstance()
            results = teach.getTeachers(status)
        except Exception as e:
            results = []
            msg = "error in manage teacher's get teachers function: " + \
                str(e)
            Logger.CreateLog(
                logging.ERROR, msg)
            pass
        finally:
            return results
