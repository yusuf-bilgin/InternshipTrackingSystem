from person import Person

class Instructor(Person):
    def __init__(self, instructorID, password, userName, phone, email, name, surname, gender, deptNo):
        super().__init__(instructorID, password, userName, phone, email, name, surname, gender)
        self.deptNo = deptNo
        
        

instructor = Instructor(5, "password", "username", "0553", "email@email", "user", "user", "male", 3)

instructor.name = "Veli"

print(instructor.userID, instructor.userName, instructor.password ,instructor.phone, 
instructor.email, instructor.name, instructor.surname, instructor.gender)