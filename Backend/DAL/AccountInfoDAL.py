from Backend.DAL.Models.AccountInfo import AccountInfo
from Backend.Database.dbConnection import mySqlConnection
from Backend.Logs.logger import Logger
from Backend.config import db
import logging


class AccountInfoDAL:
    instance = None

    def __init__(self):
        if AccountInfoDAL.instance is not None:
            raise Exception(
                "This class is a Singleton! Use getInstance() method to get the instance")
        else:
            AccountInfoDAL.instance = self

    def getInstance():
        if AccountInfoDAL.instance is None:
            AccountInfoDAL()
        return AccountInfoDAL.instance

    def createAccount(self, account: AccountInfo):
        try:
            value = account.getAccountInfo()
            db_connection = mySqlConnection.getInstance()
            connection = db_connection.db
            cursor = connection.cursor()
            pwd = value['password'].decode('UTF-8')
            addAccountInfo = f"INSERT INTO {db.configDb['databaseName']}.AccountInfo (Email,Password,Type) VALUES ('{value['email']}','{pwd}','{value['type']}')"
            cursor.execute(addAccountInfo)
            connection.commit()
            accId = cursor.lastrowid
        except Exception as e:
            msg = "Exception in AccountDAL create account function: " + str(e)
            Logger.CreateLog(
                logging.ERROR, msg)
            pass
        finally:
            if db_connection.db.is_connected():
                cursor.close
                db_connection.db.close
            return accId

    def getAccounts(self, email, type):
        try:
            query = f" SELECT Result.Email , Result.Password, Result.Id FROM ((SELECT acc.Email AS Email , acc.Password AS Password,acc.Id AS Id, acc.Type AS Type FROM {db.configDb['databaseName']}.AccountInfo AS acc JOIN {db.configDb['databaseName']}.student as std ON acc.Id = std.AccountId WHERE acc.Email  = '{email}' and std.IsApproved = 1) union (SELECT acc.Email AS Email , acc.Password AS Password,acc.Id AS Id, acc.Type AS Type FROM {db.configDb['databaseName']}.AccountInfo AS acc JOIN {db.configDb['databaseName']}.Teacher as t ON acc.Id = t.AccountId WHERE acc.Email  = '{email}' and t.IsApproved = 1)) AS Result WHERE Result.Type = '{type}'"
            # query = f"SELECT Email, Password FROM {db.configDb['databaseName']}.accountinfo where Type='{type}'"
            db_connection = mySqlConnection.getInstance()
            connection = db_connection.db
            cursor = connection.cursor()
            cursor.execute(query)
            results = cursor.fetchall()
        except Exception as e:
            results = []
            msg = "Exception in AccountDAL get accounts function: " + str(e)
            Logger.CreateLog(
                logging.ERROR, msg)
            pass
        finally:
            if db_connection.db.is_connected():
                cursor.close
                db_connection.db.close
            return results
