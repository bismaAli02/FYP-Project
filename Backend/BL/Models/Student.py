from Backend.BL.Models.Person import Person


class Student(Person):
    def __init__(self, RegNo, Name, Section, Session, Email, Password, Status=0, Type="Student"):
        super().__init__(Name, Email, Password, Type, Status)
        self._regNo = RegNo
        self._section = Section
        self._session = Session

    # def __init__(self):
    #     pass

    def getRegistrationNumber(self):
        return self._regNo

    def getSection(self):
        return self._section

    def getSession(self):
        return self._session
