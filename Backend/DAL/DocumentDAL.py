from Backend.DAL.Models.Document import Document
from Backend.Database.dbConnection import mySqlConnection
from Backend.Logs.logger import Logger
import logging
from Backend.config import db


class DocumentDAL:
    instance = None

    def __init__(self):
        if DocumentDAL.instance is not None:
            raise Exception(
                "This class is a Singleton! Use getInstance() method to get the instance")
        else:
            DocumentDAL.instance = self

    def getInstance():
        if DocumentDAL.instance is None:
            DocumentDAL()
        return DocumentDAL.instance

    def createDocument(self, document: Document):
        try:
            db_connection = mySqlConnection.getInstance()
            connection = db_connection.db
            cursor = connection.cursor()
            addDocumentQuery = f"INSERT INTO {db.configDb['databaseName']}.document (filePath) VALUES ('{document.getFilePath()}');"
            cursor.execute(addDocumentQuery)
            document_id = cursor.lastrowid
            for tag in document.getFileTags():
                addTagsQuery = f"INSERT INTO {db.configDb['databaseName']}.documentTags VALUES ({document_id},'{tag}');"
                cursor.execute(addTagsQuery)
            connection.commit()
        except Exception as e:
            msg = "Exception in DocumentDAL create document function: " + \
                str(e)
            Logger.CreateLog(
                logging.ERROR, msg)
            pass
        finally:
            if db_connection.db.is_connected():
                cursor.close
                db_connection.db.close
            return document_id
