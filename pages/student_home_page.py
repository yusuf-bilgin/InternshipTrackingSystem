from ctypes import alignment
from PyQt5.QtCore import Qt
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog
from PyQt5 import QtGui
from pages.student_announcement import StudentAnnouncementPage
from pages.student_profile_page import StudentProfilePage
from pages.student_experience_page import StudentExperiencePage
from pages.student_documents_page import StudentDocumentsPage

from page_stack import PageStack

class StudentHomePage(QDialog):
    def __init__(self, student):
        super().__init__()
        self.student = student 
        # studentID, userName, password, phone, email, name, surname, gender
        # birthdate, age, jobStatus, deptNo=None, advisorID=None, CVlink=None

        loadUi("ui_docs\\student_home_page.ui",self)

        self.outNameSurname.setText(student.name + " " + student.surname)
        self.outPhoneNumber.setText(student.phone)
        self.outEmail.setText(student.email)

        self.btnLogout.clicked.connect(self.logout)
        self.btnDocuments.clicked.connect(self.goDocumentsPage)
        self.btnExperiences.clicked.connect(self.goExperiencePage)
        self.btnProfile.clicked.connect(self.goProfilePage)
        self.btnAnnouncements.clicked.connect(self.goAnnouncementPage)

    def logout(self):
        print("logout clicked")
        pageStack = PageStack.getInstance()
        pageStack.removeWidget(self)
        pageStack.setWindowTitle("Login Page")

    def goDocumentsPage(self):
        print("go documents clicked")
        pageStack = PageStack.getInstance()
        studentDocumentsPage = StudentDocumentsPage(self.student)
        pageStack.addWidget(studentDocumentsPage)
        pageStack.setWindowTitle("Student Documents Page")
        pageStack.setCurrentIndex(pageStack.currentIndex()+1)

    def goExperiencePage(self):
        print("go experience clicked")
        pageStack = PageStack.getInstance()
        studentExperiencePage = StudentExperiencePage(self.student)
        pageStack.addWidget(studentExperiencePage)
        pageStack.setWindowTitle("Student Experiences Page")
        pageStack.setCurrentIndex(pageStack.currentIndex()+1)

    def goProfilePage(self):
        print("go profile clicked")
        pageStack = PageStack.getInstance()
        studentProfilePage = StudentProfilePage(self.student)
        pageStack.addWidget(studentProfilePage)
        pageStack.setWindowTitle("Student Profile Page")
        pageStack.setCurrentIndex(pageStack.currentIndex()+1)

    def goAnnouncementPage(self):
        print("go announcement clicked")
        pageStack = PageStack.getInstance()
        studentAnnouncementPage = StudentAnnouncementPage(self.student)
        pageStack.addWidget(studentAnnouncementPage)
        pageStack.setWindowTitle("Student Announcements Page")
        pageStack.setCurrentIndex(pageStack.currentIndex()+1)
