import Backend.Database.dbConnection
from Backend.Logs.logger import Logger
import logging
from Backend.config import db


class dbSetup:
    instance = None

    def __init__(self):
        if dbSetup.instance is not None:
            Logger.CreateLog(
                logging.ERROR, "Database class is a Singleton! Use getInstance() method to get the instance")
        else:
            dbSetup.instance = self

    def getInstance(self):
        if dbSetup.instance is None:
            dbSetup()

        return dbSetup.instance

    def databaseSetup():
        try:
            db_connection = Database.dbConnection.mySqlConnection.getInstance()
            connection = db_connection.db
            cursor = connection.cursor()
            createAccountInfoTable = f"CREATE TABLE IF NOT EXISTS {db.configDb['databaseName']}.AccountInfo (Id INT PRIMARY KEY NOT NULL AUTO_INCREMENT, Email VARCHAR(35) NOT NULL ,Password VARCHAR(255) NOT NULL, Type VARCHAR (8) , CONSTRAINT unique_constraint_email UNIQUE (Email))"
            cursor.execute(createAccountInfoTable)
            createTeacherTable = f"CREATE TABLE IF NOT EXISTS {db.configDb['databaseName']}.Teacher (Id INT PRIMARY KEY NOT NULL AUTO_INCREMENT, Name VARCHAR(35) NOT NULL, Designation VARCHAR(35), AccountId INT,IsApproved BOOLEAN , CONSTRAINT fk_field1 FOREIGN KEY (AccountId) REFERENCES documenttagging.AccountInfo (Id));"
            cursor.execute(createTeacherTable)
            createStudentTable = f"CREATE TABLE IF NOT EXISTS {db.configDb['databaseName']}.Student (Registration_Number VARCHAR(25) PRIMARY KEY, Name VARCHAR(35) NOT NULL, Section  VARCHAR(1) , Session VARCHAR(20), AccountId INT,IsApproved BOOLEAN , CONSTRAINT fk_field2 FOREIGN KEY (AccountId) REFERENCES documenttagging.AccountInfo (Id));"
            cursor.execute(createStudentTable)
            createDocumentTableQuery = f"CREATE TABLE IF NOT EXISTS {db.configDb['databaseName']}.document (Id INT PRIMARY KEY NOT NULL AUTO_INCREMENT, filePath VARCHAR(50) NOT NULL);"
            cursor.execute(createDocumentTableQuery)
            createDocumentTagsTable = f"CREATE TABLE IF NOT EXISTS {db.configDb['databaseName']}.documentTags (Document_Id INT NOT NULL, Tag VARCHAR(50) NOT NULL, CONSTRAINT fk_field3 FOREIGN KEY (Document_Id) REFERENCES documenttagging.document (Id), CONSTRAINT unique_combination UNIQUE (Document_Id, Tag))"
            cursor.execute(createDocumentTagsTable)
            createUsersDocumentTableQuery = f"CREATE TABLE IF NOT EXISTS {db.configDb['databaseName']}.usersDocument (Document_Id INT NOT NULL,AccountId INT NOT NULL, Status BOOLEAN , CONSTRAINT PRIMARY KEY (Document_Id, AccountId),CONSTRAINT fk_field4 FOREIGN KEY (Document_Id) REFERENCES documenttagging.document (Id) , CONSTRAINT fk_field5 FOREIGN KEY (AccountId) REFERENCES documenttagging.AccountInfo (Id))"
            cursor.execute(createUsersDocumentTableQuery)
            connection.commit()
        except Exception as e:
            msg = "Exception in database setup function: " + str(e)
            Logger.CreateLog(
                logging.ERROR, msg)
            pass
        finally:
            if db_connection.db.is_connected():
                cursor.close
                db_connection.db.close
