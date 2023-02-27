from PyQt5.QtCore import Qt
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QDialogButtonBox, QVBoxLayout, QLabel
from PyQt5 import QtGui

from page_stack import PageStack

class CompanyRegisterPage(QDialog):
    def __init__(self):
        super().__init__()
        loadUi("ui_docs\\company_register.ui",self)
        self.pageStack = PageStack.getInstance()

        self.btnGoBack.clicked.connect(self.goback)
        self.btnRegister.clicked.connect(self.registerCompany)

    def getInputs(self):
        username = self.inputUsername.text()
        password = self.inputPassword.text()
        confirmpassword = self.inputConfirmPassword.text()
        phone = self.inputPhone.text()
        email = self.inputEmail.text()
        cName = self.inputCompanyName.text()

        print(username, password, confirmpassword, phone, 
        email, cName)

        dataMap = {
            'username':username,
            'password':password,
            'confirmpassword':confirmpassword,
            'phone':phone,
            'email':email,
            'companyName': cName
        }

        return dataMap

    def registerCompany(self):
        # TODO check if entered data is in valid form.
        # check if there is a user having the same username, phone and email. If there is raise error.
        dataMap = self.getInputs()
        isvalid = self.validateInput(dataMap)

        if(isvalid):
            try:
                self.pageStack.dbOperations.insertUser(dataMap['username'], dataMap['password'], dataMap['phone'], dataMap['email'])
                uid = self.pageStack.dbOperations.getUserID(dataMap['username'], dataMap['password'])
                self.pageStack.dbOperations.insertCompany(uid, dataMap['companyName'])

                self.showWarning("registered")
                
            except Exception as err:
                self.showWarning(str(err))

    def validateInput(self, dataMap):
        isvalid = True
        # isEmpty?
        for key in dataMap:
            print(key, dataMap[key], str(dataMap[key]))
            if str(dataMap[key])=="":
                isvalid = False
                self.showWarning("Do not leave the field "
                                    + key + " empty!")
                
                break
        # other criterias:
        if dataMap['confirmpassword'] != dataMap['password']:
            isvalid = False
            self.showWarning("Entered passwords do not match! Check them.")
        elif len(dataMap['password']) <7 and dataMap['password'] != "":
            isvalid = False
            self.showWarning("Password must be at least 7 characters!")
        elif len(dataMap['username']) < 3:
            isvalid = False
            self.showWarning("Username must be at least 3 characters!")
        elif dataMap['email'] != "":
            if len(dataMap['email']) < 7:
                isvalid = False
                self.showWarning("Email must be at least 7 characters!")
            elif dataMap['email'].find("@") == -1 or dataMap['email'].find(".com") == -1:
                isvalid = False
                self.showWarning("There must be '@' and '.com' in the email." )
        elif dataMap['phone']!= "" and dataMap['phone'].isdigit() == False:
            isvalid = False
            self.showWarning("The phone number must consist of digits!" )
        elif dataMap['companyName']!="" and len(dataMap['companyName'])<4:
            isvalid = False
            self.showWarning("Company name must be at least 4 characters!")

        return isvalid 
    
    def showWarning(self, text):
        dlg = CustomDialog(text)
        if dlg.exec():
            print("Success!")
        else:
            print("Cancel!")

    def goback(self):
        # TODO clear the entered data
        
        self.pageStack.setWindowTitle("Register Menu Page")
        self.pageStack.removeWidget(self)



class CustomDialog(QDialog):
    def __init__(self, text, parent=None):
        super().__init__(parent)


        if text=="registered":
            self.setWindowTitle("CONGRATS :)")

            QBtn = QDialogButtonBox.Ok

            self.buttonBox = QDialogButtonBox(QBtn)
            self.buttonBox.accepted.connect(self.accept)

            self.layout = QVBoxLayout()
            message = QLabel("Succesfully Registered")
            self.layout.addWidget(message)
            self.layout.addWidget(self.buttonBox)
            self.setLayout(self.layout)

        else:
            self.setWindowTitle("Warning!")

            QBtn = QDialogButtonBox.Ok

            self.buttonBox = QDialogButtonBox(QBtn)
            self.buttonBox.accepted.connect(self.accept)

            self.layout = QVBoxLayout()
            message = QLabel(text)
            self.layout.addWidget(message)
            self.layout.addWidget(self.buttonBox)
            self.setLayout(self.layout)