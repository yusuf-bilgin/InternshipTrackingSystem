from person import Person

class Student(Person):
    def __init__(self, studentID, userName, password, phone, email, name, surname, gender, 
                            birthdate, age, jobStatus, deptNo=None, advisorID=None, CVlink=None):

        super().__init__(studentID, userName, password, phone, email, name, surname, gender)
        self.birthdate = birthdate
        self.age=age
        self.jobStatus = jobStatus
        self.deptNo = deptNo
        self.advisorID = advisorID
        self.CVlink = CVlink

student = Student(5, "password", "username", "0553", "email@email", "user", "user", "male",
                    "2001-05-17", 21, "no", deptNo=45)

student.name = "Ahmet"

student.advisorID = 7
student.CVlink = "http\\asdasd.com"

print(student.userID, student.password, student.userName, student.phone, student.email, student.name, student.surname, student.gender, 
            student.birthdate, student.age, student.jobStatus, student.deptNo, student.advisorID, student.CVlink)
