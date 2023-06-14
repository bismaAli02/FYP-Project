import mysql.connector
from Backend.config import db
from Backend.Database.db_setup import dbSetup
from Backend.Logs.logger import Logger
import logging


class mySqlConnection:
    instance = None

    def getInstance():
        if mySqlConnection.instance is None:
            mySqlConnection()
            # dbSetup.databaseSetup()
        return mySqlConnection.instance

    def __init__(self):
        self.db = None
        if mySqlConnection.instance is not None:
            raise Exception(
                "This class is a Singleton! Use getInstance() method to get the instance")
        else:
            try:
                mySqlConnection.instance = self
                self.db = mysql.connector.connection.MySQLConnection(
                    user=db.configDb["user"],
                    password=db.configDb["password"],
                    host=db.configDb["host"],
                    database=db.configDb["databaseName"])

            except Exception as e:
                msg = "Exception in database connection function: " + str(e)
                Logger.CreateLog(
                    logging.ERROR, msg)
                pass
