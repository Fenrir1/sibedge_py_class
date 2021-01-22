class Person(object):
    def __init__(self, name, phone, email, info):
        self.name = name
        self.phone = phone
        self.email = email
        self.info = info
    
    def __str__(self):
        return f'Name: {self.name}\nPhone: {self.phone}\nEmail: {self.email}\nInfo: {self.info}'

    def lower(self):
        return self.__str__()

    def toJSON(self):
        return {
            "name": self.name,
            "phone": self.phone,
            "email": self.email,
            "info": self.info
        }