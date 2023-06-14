class Teacher:
    def __init__(self, Name, Des , AccId, Status):
        self.__name = Name
        self.__designation = Des
        self.__accountId = AccId
        self.__isApproved = Status

    def getName(self):
        return self.__name
    def getDesignation(self):
        return self.__designation
    def getAccountId(self):
        return self.__accountId
    def getApprovalStatus(self):
        return self.__isApproved