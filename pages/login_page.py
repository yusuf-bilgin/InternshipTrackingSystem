from ctypes import alignment
from PyQt5.QtCore import Qt
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QDialogButtonBox, QVBoxLayout, QLabel
from PyQt5 import QtGui
from pages.instructor_home_page import InstructorHomePage
from pages.company_page import CompanyPage
from pages.student_home_page import StudentHomePage

from page_stack import PageStack

class LoginPage(QDialog):
    def __init__(self):
        super().__init__()
        loadUi("ui_docs\\login_page.ui",self)
        self.pageStack = PageStack.getInstance()

        self.btnGoBack.clicked.connect(self.goBack)
        self.btnStudentLogin.clicked.connect(self.studentLogin)
        self.btnCompanyLogin.clicked.connect(self.companyLogin)
        self.btnInstructorLogin.clicked.connect(self.instructorLogin)

        

        self.widget_2.setGraphicsEffect(self.addShadow())
        self.widget_3.setGraphicsEffect(self.addShadow())
        self.widget_4.setGraphicsEffect(self.addShadow())
        self.btnGoBack.setGraphicsEffect(self.addShadow())

    # TODO geri dönüşlerde window title'ı değiştir.
    def goBack(self):
        print("go back pressed!")
        self.pageStack.removeWidget(self)
        self.pageStack.setWindowTitle("Internship App")

    def studentLogin(self):
        print("login student clicked")
        dataMap = self.getStudentData()
        isvalid = self.validateInput(dataMap['username'], dataMap['password'])
        uid = self.pageStack.dbOperations.doesUserExist(dataMap['username'], dataMap['password'])

        if isvalid and uid != -1:
            student = self.pageStack.dbOperations.getStudent(uid)
            studentHomePage = StudentHomePage(student)
            self.pageStack.addWidget(studentHomePage)
            self.pageStack.setWindowTitle("Student Home Page")
            self.pageStack.setCurrentIndex(self.pageStack.currentIndex()+1)
            self.clearInputs()
        else:
            self.showWarning("No such student found.")
        


    def companyLogin(self):
        print("login company clicked")
        dataMap = self.getCompanyData()
        isvalid = self.validateInput(dataMap['username'], dataMap['password'])
        uid = self.pageStack.dbOperations.doesUserExist(dataMap['username'], dataMap['password'])

        if isvalid and uid != -1:
            company = self.pageStack.dbOperations.getCompany(uid)
            companyHomePage = CompanyPage(company)
            self.pageStack.addWidget(companyHomePage)
            self.pageStack.setWindowTitle("Company Home Page")
            self.pageStack.setCurrentIndex(self.pageStack.currentIndex()+1)
            self.clearInputs()
        else:
            self.showWarning("No such company found.")


    def instructorLogin(self):
        print("login instructor clicked")
        dataMap = self.getInstructorData()
        isvalid = self.validateInput(dataMap['username'], dataMap['password'])
        uid = self.pageStack.dbOperations.doesUserExist(dataMap['username'], dataMap['password'])

        if isvalid and uid != -1:
            instructor = self.pageStack.dbOperations.getInstructor(uid)
            instructorHomePage = InstructorHomePage(instructor)
            self.pageStack.addWidget(instructorHomePage)
            self.pageStack.setWindowTitle("Instructor Home Page")
            self.pageStack.setCurrentIndex(self.pageStack.currentIndex()+1)
            self.clearInputs()
        else:
            self.showWarning("No such instructor found.")
        

    
    def getStudentData(self):

        username = self.inputUsernameStudent.text()
        password = self.inputPasswordStudent.text()

        dataMap = {'username': username, 'password':password}

        return dataMap

    def getCompanyData(self):
        username = self.inputUsernameCompany.text()
        password = self.inputPasswordCompany.text()

        dataMap = {'username': username, 'password':password}

        return dataMap

    def getInstructorData(self):
        username = self.inputUsernameInstructor.text()
        password = self.inputPasswordInstructor.text()

        dataMap = {'username': username, 'password':password}

        return dataMap

    def validateInput(self, username, password):
        if username != "" and password != "":
            return True
        else:
            return False

    def clearInputs(self):
        self.inputUsernameCompany.setText("")
        self.inputPasswordCompany.setText("")

        self.inputUsernameInstructor.setText("")
        self.inputPasswordInstructor.setText("")

        self.inputUsernameStudent.setText("")
        self.inputPasswordStudent.setText("")



    # TODO add shadow metodunu ayrı bir classta yaz. Parametre olarak list of QWidgets alsın.
    # bir döngü ile her bir widget için aşağıdaki kodu çalıştırıp shadow eklesin.
    def addShadow(self):
        shadow = QtWidgets.QGraphicsDropShadowEffect(self)
        shadow.setBlurRadius(12)
        shadow.setColor(QtGui.QColor(76, 35, 45).lighter())
        shadow.setOffset(8)
        return shadow

    def showWarning(self, text):
        dlg = CustomDialog(text)
        if dlg.exec():
            print("Success!")
        else:
            print("Cancel!")




class CustomDialog(QDialog):
    def __init__(self, text, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Warning!")

        QBtn = QDialogButtonBox.Ok

        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)

        self.layout = QVBoxLayout()
        message = QLabel(text)
        self.layout.addWidget(message)
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)