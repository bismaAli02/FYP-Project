from Backend.Database.dbConnection import mySqlConnection
from Backend.DAL.Models.Teacher import Teacher
from Backend.Logs.logger import Logger
import logging
from Backend.config import db


class TeacherDAL:
    instance = None

    def __init__(self):
        if TeacherDAL.instance is not None:
            raise Exception(
                "This class is a Singleton! Use getInstance() method to get the instance")
        else:
            TeacherDAL.instance = self

    def getInstance():
        if TeacherDAL.instance is None:
            TeacherDAL()
        return TeacherDAL.instance

    def createTeacher(self, teacher: Teacher, accountId):
        try:
            db_connection = mySqlConnection.getInstance()
            connection = db_connection.db
            cursor = connection.cursor()
            addTeacher = f"INSERT INTO {db.configDb['databaseName']}.Teacher (Name,Designation,AccountId,IsApproved) VALUES ('{teacher.getName()}','{teacher.getDesignation()}',{accountId},{teacher.getApprovalStatus()})"
            cursor.execute(addTeacher)
            connection.commit()
        except Exception as e:
            msg = "Exception in TeacherDAL create teacher account function: " + \
                str(e)
            Logger.CreateLog(
                logging.ERROR, msg)
            pass
        finally:
            if db_connection.db.is_connected():
                cursor.close
                db_connection.db.close

    def updateTeacherStatus(self, status, teacherId):
        try:
            query = f"UPDATE {db.configDb['databaseName']}.Teacher SET IsApproved = {status} WHERE Id = '{teacherId}'"
            db_connection = mySqlConnection.getInstance()
            connection = db_connection.db
            cursor = connection.cursor()
            cursor.execute(query)
            connection.commit()
        except Exception as e:
            msg = "Exception in TeacherDAL update teacher account function: " + \
                str(e)
            Logger.CreateLog(
                logging.ERROR, msg)
            pass
        finally:
            if db_connection.db.is_connected():
                cursor.close
                db_connection.db.close

    def getTeacherId(self, email):
        try:
            query = f"SELECT t.Id  FROM {db.configDb['databaseName']}.Teacher AS t  JOIN {db.configDb['databaseName']}.accountinfo AS acc ON t.AccountId = acc.Id  WHERE acc.Email = '{email}'"
            db_connection = mySqlConnection.getInstance()
            connection = db_connection.db
            cursor = connection.cursor()
            cursor.execute(query)
            result = cursor.fetchall()
        except Exception as e:
            result = 0
            msg = "Exception in AccountDAL get Teacher Id account function: " + \
                str(e)
            Logger.CreateLog(
                logging.ERROR, msg)
            pass
        finally:
            if db_connection.db.is_connected():
                cursor.close
                db_connection.db.close
            return result

    def getTeachers(self, status):
        try:
            query = f"SELECT t.Name,t.Designation ,acc.Email,t.AccountId  FROM {db.configDb['databaseName']}.Teacher AS t  JOIN {db.configDb['databaseName']}.accountinfo AS acc ON t.AccountId = acc.Id  WHERE t.IsApproved = {status}"
            db_connection = mySqlConnection.getInstance()
            connection = db_connection.db
            cursor = connection.cursor()
            cursor.execute(query)
            results = cursor.fetchall()
        except Exception as e:
            results = []
            msg = "Exception in AccountDAL get student account function: " + \
                str(e)
            Logger.CreateLog(
                logging.ERROR, msg)
            pass
        finally:
            if db_connection.db.is_connected():
                cursor.close
                db_connection.db.close
            return results
