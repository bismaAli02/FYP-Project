from Backend.BL.Models.Document import Document
from Backend.DAL.DocumentDAL import DocumentDAL
from Backend.DAL.StudentDAL import studentDAL
from Backend.DAL.TeacherDAL import TeacherDAL
from Backend.BL.Services.emailServices import emailServices
from Backend.DAL.UsersDocumentDAL import UsersDocumentDAL
from Backend.config import db
from Backend.Logs.logger import Logger
import logging

import shutil


class manageDocument:

    def createDocument(self, document: Document):
        try:
            userDoc = UsersDocumentDAL.getInstance()
            doc = DocumentDAL.getInstance()
            docId = doc.createDocument(document)
            self.storeFile(document.getSourcePath(), document.getFilePath())
            names, emails, accountId = self.getTaggedUsers(
                document)
            for i in range(0, len(accountId)):
                userDoc.addUsersDocument(docId, accountId[i], 0)

            send = emailServices.getInstance()
            for i in range(0, len(names)):
                send.sendEmailMessage(
                    db.configEmail["sourceAddress"], db.configEmail["password"], emails[i], names[i])
        except Exception as e:
            msg = "Exception in manage document's create document function: " + \
                str(e)
            Logger.CreateLog(
                logging.ERROR, msg)
            pass

    def storeFile(self, sourceFilePath, destinationFilePath):
        try:
            shutil.copy(sourceFilePath, destinationFilePath)
        except Exception as e:
            msg = "Exception in manage document's store function: " + \
                str(e)
            Logger.CreateLog(
                logging.ERROR, msg)
            pass

    def getTaggedUsers(self, document: Document):
        try:
            accountId = []
            emails = []
            names = []
            student_elements = [element.split(
                ".")[1] for element in document.getFileTags() if "Student." in element]
            teacher_elements = [element.split(
                ".")[1] for element in document.getFileTags() if "Teacher." in element]
            student = studentDAL.getInstance()
            stdResult = student.getStudents(1)
            for i in student_elements:
                for j in stdResult:
                    if (j[0] == i or j[3] == i or j[4] == i):
                        emails.append(j[2])
                        names.append(j[1])
                        accountId.append(j[6])
            teacher = TeacherDAL.getInstance()
            teacherResult = teacher.getTeachers(1)
            for i in teacher_elements:
                for j in teacherResult:
                    if (j[0] == i):
                        emails.append(j[2])
                        names.append(j[0])
                        accountId.append(j[3])

        except Exception as e:
            names = []
            emails = []
            msg = "Exception in manage document's get tagged users email function: " + \
                str(e)
            Logger.CreateLog(
                logging.ERROR, msg)
            pass
        finally:
            return list(set(names)), list(set(emails)), list(set(accountId))

    def UpdateDocumentStatus(self, userId, documentId):
        try:
            userDoc = UsersDocumentDAL.getInstance()
            print(userId)
            print(documentId)
            userDoc.updateDocumentStatus(userId, documentId)
        except Exception as e:
            msg = "Exception in manage document's update document status function: " + \
                str(e)
            Logger.CreateLog(
                logging.ERROR, msg)
            pass
