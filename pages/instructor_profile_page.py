from ctypes import alignment
from PyQt5.QtCore import Qt
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5 import QtGui

from page_stack import PageStack

class InstructorProfilePage(QDialog):
    def __init__(self, instructor):
        super().__init__()
        self.instructor = instructor
        loadUi("ui_docs\\instructor_profile_page.ui",self)

        self.btnGoBack.clicked.connect(self.goback)

    def goback(self):
        print("go back pressed!")
        pageStack = PageStack.getInstance()
        pageStack.removeWidget(self)
        pageStack.setWindowTitle("Instructor Home Page")