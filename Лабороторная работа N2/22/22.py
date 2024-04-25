import re


class Validator:
    def isEmail(self, email):
        if str(email).find('email.') > -1:
            return True
        else:
            return False

    def isDomain(self, domain):
        pass

    def isNumber(self, number):
        number = re.match(r'\+7[0-9]{3}', number)
        return number is not None


validator = Validator()
print(validator.isEmail("Dima@email.com"))
print(validator.isEmail("Dima@eail.com"))


print(3223)
print(7323)
