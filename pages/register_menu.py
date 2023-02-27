from ctypes import alignment
from PyQt5.QtCore import Qt
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.QtGui import QPixmap
from pages.instructor_register_page import InstructorRegisterPage
from pages.company_register_page import CompanyRegisterPage
from pages.student_register import StudentRegisterPage

from page_stack import PageStack

class RegisterMenu(QDialog):
    def __init__(self):
        super().__init__()
        loadUi("ui_docs\\register_menu_page.ui",self)
        
        # mainLayout = self.column
        # self.setLayout(mainLayout)

        # vLayout = QtWidgets.QVBoxLayout()
        
        # widget = QtWidgets.QWidget()
        # widget.setLayout(self.column)

        # vLayout.addWidget(widget, alignment=Qt.AlignCenter)

        # self.setLayout(vLayout)

        self.btnGoBack.clicked.connect(self.goBack)
        self.btnRegisterStudent.clicked.connect(self.goStudentRegisterPage)
        self.btnRegisterInstructor.clicked.connect(self.goInstructorRegisterPage)
        self.btnRegisterCompany.clicked.connect(self.goCompanyRegisterPage)

    def goStudentRegisterPage(self):
        print("student register pressed")
        studentRegisterPage = StudentRegisterPage()
        pageStack = PageStack.getInstance()
        pageStack.addWidget(studentRegisterPage)
        pageStack.setWindowTitle("Student Register Page")
        pageStack.setCurrentIndex(pageStack.currentIndex()+1)

    def goInstructorRegisterPage(self):
        print("instructor register pressed")
        instructorRegisterPage = InstructorRegisterPage()
        pageStack = PageStack.getInstance()
        pageStack.addWidget(instructorRegisterPage)
        pageStack.setWindowTitle("Instructor Register Page")
        pageStack.setCurrentIndex(pageStack.currentIndex()+1)

    def goCompanyRegisterPage(self):
        print("company register pressed")
        companyRegisterPage = CompanyRegisterPage()
        pageStack = PageStack.getInstance()
        pageStack.addWidget(companyRegisterPage)
        pageStack.setWindowTitle("Company Register Page")
        pageStack.setCurrentIndex(pageStack.currentIndex()+1)    

    def goBack(self):
        print("goBack clicked")
        pageStack = PageStack.getInstance()
        pageStack.removeWidget(self)
        pageStack.setWindowTitle("Internship App")