from Backend.Database.dbConnection import mySqlConnection
from Backend.DAL.Models.Student import Student
import logging
from Backend.Logs.logger import Logger
from Backend.config import db


class studentDAL:
    instance = None

    def __init__(self):
        if studentDAL.instance is not None:
            raise Exception(
                "This class is a Singleton! Use getInstance() method to get the instance")
        else:
            studentDAL.instance = self

    def getInstance():
        if studentDAL.instance is None:
            studentDAL()
        return studentDAL.instance

    def createStudentAccount(self, student: Student, accountId):
        try:
            db_connection = mySqlConnection.getInstance()
            connection = db_connection.db
            cursor = connection.cursor()
            addStudent = f"INSERT INTO {db.configDb['databaseName']}.Student (Registration_Number, Name, Section, Session,AccountId,IsApproved) VALUES ('{student.getRegistrationNumber()}','{student.getName()}','{student.getSection()}','{student.getSession()}',{accountId},{student.getApprovalStatus()})"
            cursor.execute(addStudent)
            connection.commit()
        except Exception as e:
            msg = "Error in StudentDAL Create Student Account Funtion: " + \
                str(e)
            Logger.CreateLog(
                logging.ERROR, msg)
            pass
        finally:
            if db_connection.db.is_connected():
                cursor.close
                db_connection.db.close

    def updateStudentStatus(self, status, registrationNumber):
        try:
            query = f"UPDATE {db.configDb['databaseName']}.student SET IsApproved = {status} WHERE Registration_Number = '{registrationNumber}'"
            db_connection = mySqlConnection.getInstance()
            connection = db_connection.db
            cursor = connection.cursor()
            cursor.execute(query)
            connection.commit()
        except Exception as e:
            msg = "Error in StudentDAL Update Student Status Function: " + \
                str(e)
            Logger.CreateLog(
                logging.ERROR, msg)
            pass
        finally:
            if db_connection.db.is_connected():
                cursor.close
                db_connection.db.close

    def getStudents(self, status):
        try:
            query = f"SELECT std.Registration_Number, std.Name ,acc.Email , std.Section , std.Session , std.IsApproved , acc.Id FROM {db.configDb['databaseName']}.student AS std JOIN {db.configDb['databaseName']}.accountinfo AS acc ON std.AccountId = acc.Id  WHERE std.IsApproved = {status}"
            db_connection = mySqlConnection.getInstance()
            connection = db_connection.db
            cursor = connection.cursor()
            cursor.execute(query)
            results = cursor.fetchall()
        except Exception as e:
            msg = "Exception in StudentDAL get student function: " + str(e)
            Logger.CreateLog(
                logging.ERROR, msg)
            results = []
            pass
        finally:
            if db_connection.db.is_connected():
                cursor.close
                db_connection.db.close
            return results

    def getStudentSession(self):
        try:
            query = f"SELECT distinct Session FROM {db.configDb['databaseName']}.student where IsApproved=1;"
            db_connection = mySqlConnection.getInstance()
            connection = db_connection.db
            cursor = connection.cursor()
            cursor.execute(query)
            results = cursor.fetchall()
        except Exception as e:
            msg = "Exception in StudentDAL get student session function: " + str(e)
            Logger.CreateLog(
                logging.ERROR, msg)
            results = []
            pass
        finally:
            if db_connection.db.is_connected():
                cursor.close
                db_connection.db.close
            return results
