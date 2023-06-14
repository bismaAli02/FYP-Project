from Backend.Database.dbConnection import mySqlConnection
from Backend.config import db
from Backend.Logs.logger import Logger
import logging


class UsersDocumentDAL:
    instance = None

    def __init__(self):
        if UsersDocumentDAL.instance is not None:
            raise Exception(
                "This class is a Singleton! Use getInstance() method to get the instance")
        else:
            UsersDocumentDAL.instance = self

    def getInstance():
        if UsersDocumentDAL.instance is None:
            UsersDocumentDAL()
        return UsersDocumentDAL.instance

    def addUsersDocument(self, documentId, accountId, status):
        try:
            db_connection = mySqlConnection.getInstance()
            connection = db_connection.db
            cursor = connection.cursor()
            addUsersDoc = f"INSERT INTO {db.configDb['databaseName']}.usersDocument (Document_Id,AccountId,Status) VALUES ({documentId},{accountId},{status})"
            cursor.execute(addUsersDoc)
            connection.commit()
        except Exception as e:
            msg = "Exception in UsersDocumentDAL's add users document function: " + \
                str(e)
            Logger.CreateLog(
                logging.ERROR, msg)
            pass
        finally:
            if db_connection.db.is_connected():
                cursor.close
                db_connection.db.close

    def getUsersDocument(self, email, status):
        try:
            db_connection = mySqlConnection.getInstance()
            connection = db_connection.db
            cursor = connection.cursor()
            usersDoc = f"SELECT table2.filePath , table1.Id FROM (SELECT doc.Document_Id AS Id FROM documenttagging.accountInfo AS acc JOIN  documenttagging.usersdocument AS doc ON acc.Id = doc.AccountId WHERE acc.Email = '{email}' and doc.Status = {status}) AS table1 JOIN documenttagging.document AS table2 ON table1.Id = table2.Id"
            cursor.execute(usersDoc)
            results = cursor.fetchall()
        except Exception as e:
            results = []
            msg = "Exception in UsersDocumentDAL's get users document function: " + \
                str(e)
            Logger.CreateLog(
                logging.ERROR, msg)
            pass
        finally:
            if db_connection.db.is_connected():
                cursor.close
                db_connection.db.close
            return results

    def updateDocumentStatus(self, userId, documentId):
        try:
            db_connection = mySqlConnection.getInstance()
            connection = db_connection.db
            cursor = connection.cursor()
            print("here")
            print(userId)
            print(documentId)
            query = f"UPDATE {db.configDb['databaseName']}.usersdocument SET Status=1 WHERE Document_Id={documentId} AND AccountId=6"
            Logger.CreateLog(
                logging.ERROR, query)
            n = cursor.execute(query)
            Logger.CreateLog(
                logging.ERROR, n)
            # results = cursor.fetchall()
        except Exception as e:
            # results = []
            msg = "Exception in UsersDocumentDAL's get users document function: " + \
                str(e)
            Logger.CreateLog(
                logging.ERROR, msg)
            pass
        finally:
            if db_connection.db.is_connected():
                cursor.close
                db_connection.db.close
            # return results
