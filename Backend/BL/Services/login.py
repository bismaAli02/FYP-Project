from Backend.DAL.AccountInfoDAL import AccountInfoDAL
from Backend.BL.Services.encryption import encryption
from Backend.DAL.UsersDocumentDAL import UsersDocumentDAL
import appdirs
import json
import os
import datetime
from Backend.Logs.logger import Logger
import logging
import bcrypt


class loginServices:

    def storeCredentials(self, email, password):
        try:
            expiration_time = datetime.datetime.now() + datetime.timedelta(hours=24)
            data = {
                "email": email,
                "password": password,
                "expiration_time": expiration_time.isoformat()
            }
            data_dir = appdirs.user_data_dir(appname="app")
            os.makedirs(data_dir, exist_ok=True)
            file_path = os.path.join(data_dir, "credentials.json")
            with open(file_path, "w") as file:
                json.dump(data, file)
        except Exception as e:
            msg = "Exception in store credentials function: " + str(e)
            Logger.CreateLog(
                logging.ERROR, msg)
            pass

    def retrieveCredentials(self):
        try:
            data_dir = appdirs.user_data_dir(appname="app")
            # print(data_dir)
            file_path = os.path.join(data_dir, "credentials.json")
            if (os.path.exists(file_path)):
                with open(file_path, "r") as file:
                    data = json.load(file)
                email = data["email"]
                password = data["password"]
                expiration_time = datetime.datetime.fromisoformat(
                    data["expiration_time"])
                return email, password, expiration_time, True
            else:
                return None
        except Exception as e:
            msg = "Exception in retrived credentials function: " + str(e)
            Logger.CreateLog(
                logging.ERROR, msg)
            pass

    def check(self, credentials):
        if credentials is not None:
            if datetime.datetime.now() > credentials[2]:
                return True
        return False

    def checkLoginCredentials(self, email, password, type):
        try:
            credentials = self.retrieveCredentials()
            userDoc = UsersDocumentDAL.getInstance()
            userId = 0
            # while (True):
            if credentials is None or self.check(credentials):
                # email, password = menu()
                if password != "":
                    pwd = password.encode('utf-8')
                    acc = AccountInfoDAL.getInstance()
                    user = acc.getAccounts(email, type)
                    checkEmail = False
                    checkPass = False
                    print(user)
                    for row in user:
                        print(row)
                        if (row[0] == email):
                            checkEmail = True
                            storedPassword = row[1].encode(
                                'utf-8')
                            validate = bcrypt.checkpw(pwd, storedPassword)
                            if (validate == True):
                                self.storeCredentials(
                                    email, encryption.encryptedPassword(password).decode('utf-8'))
                                checkPass = True
                                userId = row[2]
                                print("hello")
                                break
                            else:
                                print("Wrong Password")
                                # break

                    if (checkEmail is not True):
                        print("User with this email does not exist")
                        # break
                    if (checkPass == True):
                        result = userDoc.getUsersDocument(email, 0)
                        # break
                else:
                    print("Password must be entered")
            else:
                result = userDoc.getUsersDocument(credentials[0], 0)
                self.storeCredentials(
                    credentials[0], credentials[1])
                # break

        except Exception as e:
            result = []
            msg = "Exception in check login credentials function: " + str(e)
            Logger.CreateLog(
                logging.ERROR, msg)
            pass
        finally:
            return result, userId
