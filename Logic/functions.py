from Backend.BL.Models.Student import Student
from Backend.BL.Models.Teacher import Teacher
from Backend.BL.Models.Document import Document
from Backend.BL.manageStudent import manageStudent
from Backend.BL.manageTeacher import manageTeacher
from Backend.BL.manageDocument import manageDocument
from Backend.BL.Services.login import loginServices
from Backend.Logs.logger import Logger
import logging


class functions:
    def creatStudent(name, registrationNumber, email, password, section, session):
        try:
            std = Student(registrationNumber, name, section,
                          session, email, password, 0, "Student")
            m = manageStudent()
            m.createStudentAccount(std)
            return True
        except Exception as e:
            msg = "Exception in function's class Create Student Function : " + \
                str(e)
            Logger.CreateLog(
                logging.ERROR, msg)
            return False
        pass

    def createTeacher(name,designation, email, password):
        try:
            teacher = Teacher(name,designation, email, password, 0, "Teacher")
            m = manageTeacher()
            m.createTeacher(teacher)

        except Exception as e:
            msg = "Exception in function's class Create Teacher Function : " + \
                str(e)
            Logger.CreateLog(
                logging.ERROR, msg)
        pass

    def getStudentStatus(status):
        try:
            m = manageStudent()
            results = m.getStudents(status)
        except Exception as e:
            results = []
            msg = "Exception in function's class get Student Function : " + \
                str(e)
            Logger.CreateLog(
                logging.ERROR, msg)
            pass

        finally:
            return results

    def getStudentSession():
        try:
            m = manageStudent()
            results = m.getStudentSession()
        except Exception as e:
            results = []
            msg = "Exception in function's class get Student session Function : " + \
                str(e)
            Logger.CreateLog(
                logging.ERROR, msg)
            pass

        finally:
            return results

    def GetTeacherId(email):
        try:
            m=manageTeacher()
            result=m.GetTeacherId(email)
        except Exception as e:
            result=0
            msg = "Exception in function's class get teacher Id Function : " + \
                str(e)
            Logger.CreateLog(
                logging.ERROR, msg)
            pass
        finally:
            return result

    def getTeachersStatus(status):
        try:
            m = manageTeacher()
            results = m.getTeachers(status)
        except Exception as e:
            results = []
            msg = "Exception in function's class get teacher Function : " + \
                str(e)
            Logger.CreateLog(
                logging.ERROR, msg)
            pass
        finally:
            return results

    def approvedStudent(status, registrationNumber):
        try:
            m = manageStudent()
            m.updateStudentStatus(status, registrationNumber)
        except Exception as e:
            msg = "Exception in function's class approved student Function : " + \
                str(e)
            Logger.CreateLog(
                logging.ERROR, msg)
            pass

    def approvedTeacher(status, teacherId):
        try:
            m = manageTeacher()
            m.updateTeacherStatus(status, teacherId)
        except Exception as e:
            msg = "Exception in function's class approved teacher Function : " + \
                str(e)
            Logger.CreateLog(
                logging.ERROR, msg)
            pass

    def createDocument(doc: Document):
        try:
            manageDoc = manageDocument()
            manageDoc.createDocument(doc)
        except Exception as e:
            msg = "Exception in function's class create document Function : " + \
                str(e)
            Logger.CreateLog(
                logging.ERROR, msg)
            pass

    def userLoggin(email, password, type):
        isLoggedIn=False
        try:
            login = loginServices()
            userDocuments,userId = login.checkLoginCredentials(email, password, type)
            isLoggedIn=True
        except Exception as e:
            userDocuments = []
            msg = "Exception in function's class user loggin Function : " + \
                str(e)
            Logger.CreateLog(logging.ERROR, msg)
            pass
        finally:
            return userDocuments,isLoggedIn,userId

    def UpdateDocumentStatus(userId,documentId):
        try:
            manageDoc = manageDocument()
            manageDoc.UpdateDocumentStatus(userId,documentId)
        except Exception as e:
            msg = "Exception in function's class Update Document Status Function : " + \
                str(e)
            Logger.CreateLog(logging.ERROR, msg)
            pass
