from user import User

class Person(User):
    def __init__(self, personID, userName, password, phone, email, name, surname, gender):
        super().__init__(personID, userName, password, phone, email)
        self.name = name
        self.surname = surname
        self.gender = gender
        

person = Person(5, "password", "username", "0553", "email@email", "user", "user", "male")

person.name = "ali"

print(person.userID, person.userName, person.password ,person.phone, 
person.email, person.name, person.surname, person.gender)