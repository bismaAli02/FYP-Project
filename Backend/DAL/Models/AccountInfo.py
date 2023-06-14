class AccountInfo:
    def __init__(self, Email, Password, Type):
        self.__email = Email
        self.__password = Password
        self.__type = Type

    def getAccountInfo(self):
        return {
            'email': self.__email,
            'password': self.__password,
            'type': self.__type
        }
