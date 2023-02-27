from user import User

class Company(User):
    def __init__(self, companyID, password, userName, phone, email, cName):
        super().__init__(companyID, password, userName, phone, email)
        self.cName = cName

company = Company(8, "password", "company", "021254 54 54", "asd@sd", "trendyol")

print(company.userID, company.userName, company.password ,company.phone, 
company.email, company.cName)