import bcrypt
from Backend.Logs.logger import Logger
import logging


class encryption:
    def encryptedPassword(pwd):
        try:
            bytes = pwd.encode('utf-8')
            # generating the salt
            salt = bcrypt.gensalt()
            # Hashing the password
            hash = bcrypt.hashpw(bytes, salt)
        except Exception as e:
            hash = ""
            msg = "Exception in Encryption Service's Encrypted Password Function " + \
                str(e)
            Logger.CreateLog(
                logging.ERROR, msg)
            pass
        finally:
            return hash
