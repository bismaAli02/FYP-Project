from datetime import date


class Validations:
    @staticmethod
    def PasswordValidation(password):
        count = 0
        for p in password:
            count += 1
        for x in password:
            if ((x == "@" or x == "!" or x == "#" or x == "%" or x == "^" or x == "&" or x == "*" or x == "$" or
                    x == "+" or x == "-" or x == ".") and count >= 8):
                return True
        return False

    @staticmethod
    def NameValidation(name):
        flag = False
        count = 0
        for p in name:
            count += 1
        for p in name:
            if(((ord(p) >= 65 and ord(p) <= 90) or (ord(p) >= 97 and ord(p) <= 122) or ord(p) == 32) and count >= 3):
                flag = True
            else:
                flag = False
                break
        return flag

    @staticmethod
    def DepartmentCheck(department):
        dep = ["-CS-", "-CE-", "-ME-", "-EE-", "GE", "-CD-CS-",
               "-CD-CE-", "-CD-ME-", "-CD-EE-", "-CD-GE-"]
        for i in range(len(dep)):
            if department == dep[i]:
                return True
        return False

    @staticmethod
    def RegisterNoValidations(regNo):
        isValid = True
        if len(regNo) < 9:
            print("Registration No does no fit up to the required Lenght")
            isValid = False
        else:
            year = regNo[:4]
            year1 = 0
            startIdx = 0
            endIdx = 0
            found = False
            for r in range(len(regNo)):
                if (regNo[r] == "-" and not found):
                    startIdx = r
                    found = True
                if (regNo[r] == "-" and (regNo[r+1] == "0" or regNo[r+1] == "1" or regNo[r+1] == "2" or regNo[r+1] == "3" or regNo[r+1] == "4" or regNo[r+1] == "5" or regNo[r+1] == "6" or regNo[r+1] == "7" or regNo[r+1] == "8" or regNo[r+1] == "9") and found):
                    endIdx = r

            department = regNo[startIdx:endIdx+1]
            regNumb = 0
            regNumb1 = regNo[endIdx+1:]
            year1 = Validations.try_parse_int(year)
            if year1 is None:
                isValid = False
                return isValid
            currentYear = date.today().year
            if ((year1 < currentYear - 4) or year1 >= currentYear):
                isValid = False
                return isValid

            if not (Validations.DepartmentCheck(department)):
                isValid = False
                return isValid
            regNumb = Validations.try_parse_int(regNumb1)
            if regNumb is None:
                isValid = False
                return isValid
        return isValid

    @staticmethod
    def try_parse_int(year):
        try:
            return int(year)
        except (ValueError, TypeError):
            return None

    @staticmethod
    def EmailValidation(email):
        isValid = False
        if ("@" in email and (email[-4:] == ".com" or email[-3:] == ".pk")):
            isValid = True
        return isValid

    @staticmethod
    def SessionValidation(session, regNo):
        isValid = False
        year = regNo[:4]
        if (session == year):
            isValid = True
        return isValid

    @staticmethod
    def SectionValidation(section):
        isValid = False
        if (len(section) == 1 and (ord(section) >= 65 and ord(section) <= 90)):
            isValid = True
        return isValid
