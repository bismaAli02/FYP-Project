from Backend.BL.Models.AccountInfo import AccountInfo


class Person:
    def __init__(self, Name, Email, Password, Type, Status):
        self._name = Name
        self._accountInfo = AccountInfo(
            Email, Password, Type)
        self._isApproved = Status

    def getName(self):
        return self._name

    def getAccountInfo(self):
        return {
            'email': self._accountInfo.getEmail(),
            'password':  self._accountInfo.getPassword(),
            'type': self._accountInfo.getType()
        }

    def getApprovalStatus(self):
        return self._isApproved

    def setPassword(self, pwd):
        self._accountInfo.setPassword(pwd)
