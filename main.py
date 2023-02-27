import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.QtGui import QPixmap

from page_stack import PageStack
from pages.register_menu import RegisterMenu
from pages.login_page import LoginPage

class HomePage(QDialog):
    
    def __init__(self):
        super().__init__()
        loadUi("ui_docs\\starting_page.ui",self)

        #self.pageStack = PageStack.getInstance()
        
        # mainLayout = self.column
        # self.setLayout(mainLayout)
        self.btnRegister.clicked.connect(self.goRegister)
        self.btnLogin.clicked.connect(self.goLogin)

    def goRegister(self):
        print("register clicked")
        registerMenu = RegisterMenu()
        pageStack.addWidget(registerMenu)
        pageStack.setWindowTitle("Register Menu Page")
        pageStack.setCurrentIndex(pageStack.currentIndex()+1)
        
    def goLogin(self):
        print("login clicked")
        loginPage = LoginPage()
        pageStack.addWidget(loginPage)
        pageStack.setWindowTitle("Login Page")
        pageStack.setCurrentIndex(pageStack.currentIndex()+1)  


app = QApplication(sys.argv)
pageStack = PageStack.getInstance()
homePage = HomePage()
pageStack.addWidget(homePage)
pageStack.setWindowTitle("Internship App")
pageStack.setWindowIcon(QIcon('icon.jpeg'))

pageStack.dbOperations.getAllUsers()

pageStack.show()


try:
    sys.exit(app.exec_())
except:
    print("Exiting")
