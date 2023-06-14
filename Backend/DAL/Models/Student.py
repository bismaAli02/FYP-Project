class Student:
    def __init__(self, Reg_No, Name, Sec, Sess, AccId,Status):
        self.__regNo = Reg_No
        self.__name = Name
        self.__section = Sec
        self.__session = Sess
        self.__accountId = AccId
        self.__isApproved = Status
    def getRegistrationNumber(self):
        return self.__regNo
    def getName(self):
        return self.__name
    def getSection(self):
        return self.__section
    def getSession(self):
        return self.__session
    def getAccountId(self):
        return self.__accountId
    def getApprovalStatus(self):
        return self.__isApproved