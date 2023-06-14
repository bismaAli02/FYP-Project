class AccountInfo:
    def __init__(self, Email, Password, Type):
        self._email = Email
        self._password = Password
        self._type = Type

    def getEmail(self):
        return self._email

    def getPassword(self):
        return self._password

    def getType(self):
        return self._type

    def setPassword(self, pwd):
        self._password = pwd
