from ctypes import alignment
from PyQt5.QtCore import Qt
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5 import QtGui
from pages.instructor_profile_page import InstructorProfilePage
from pages.instructor_announcement_page import InstructorAnnouncementPage
from pages.instructor_approval_page import InstructorApprovalPage

from page_stack import PageStack

class InstructorHomePage(QDialog):
    def __init__(self, instructor):
        super().__init__()
        self.instructor = instructor
        loadUi("ui_docs\\instructor_home_page.ui",self)

        self.welcome.setText("WELCOME " + self.instructor.name + " " + self.instructor.surname)

        self.btnLogout.clicked.connect(self.logout)
        self.btnGoAnnouncementPage.clicked.connect(self.goAnnouncementPage)
        self.btnGoCheckDocumentsPage.clicked.connect(self.goApprovalPage)
        #self.btnProfile.clicked.connect(self.goProfilePage)

    def logout(self):
        print("logout pressed")
        pageStack = PageStack.getInstance()
        pageStack.setWindowTitle("Login Page")
        pageStack.removeWidget(self)

    def goAnnouncementPage(self):
        print("go announcement page clicked")
        pageStack = PageStack.getInstance()
        instructorAnnouncementPage = InstructorAnnouncementPage(self.instructor)
        pageStack.addWidget(instructorAnnouncementPage)
        pageStack.setWindowTitle("Approval Page")
        pageStack.setCurrentIndex(pageStack.currentIndex()+1)
        InstructorAnnouncementPage

    def goApprovalPage(self):
        print("go approval page clicked")
        pageStack = PageStack.getInstance()
        instructorApprovalPage = InstructorApprovalPage(self.instructor)
        pageStack.addWidget(instructorApprovalPage)
        pageStack.setWindowTitle("Approval Page")
        pageStack.setCurrentIndex(pageStack.currentIndex()+1)

    def goProfilePage(self):
        print("go profile page clicked")
        pageStack = PageStack.getInstance()
        instructorProfilePage = InstructorProfilePage(self.instructor)
        pageStack.addWidget(instructorProfilePage)
        pageStack.setWindowTitle("Profile Page")
        pageStack.setCurrentIndex(pageStack.currentIndex()+1)
        