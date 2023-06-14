from Backend.BL.Models.Person import Person


class Teacher(Person):
    def __init__(self, Name, Designation, Email, Password, Status, Type):
        super().__init__(Name, Email,  Password, Type, Status)
        self._designation = Designation

    def getDesignation(self):
        return self._designation
