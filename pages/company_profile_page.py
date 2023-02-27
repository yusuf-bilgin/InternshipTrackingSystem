from PyQt5.QtCore import Qt
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog
from PyQt5 import QtGui

from page_stack import PageStack

class CompanyProfilePage(QDialog):
    def __init__(self, companyID):
        super().__init__()
        self.companyID = companyID
        loadUi("ui_docs\\company_profile_page.ui",self)
        self.pageStack = PageStack.getInstance()

        self.btnGoBack.clicked.connect(self.goback)
        self.btnUpdateAdress.clicked.connect(self.updateAdress)
        self.btnUpdateEmail.clicked.connect(self.updateEmail)
        self.btnUpdatePhone.clicked.connect(self.updatePhone)

    def updateAdress(self):
        # DİKKAT: Önceden girilmiş veri olmadığından update yapamıyor.
        print("update address pressed")
        postalcode = self.inputPostalCode.text()
        city = self.inputCity.text()
        street = self.inputStreet.text()
        aptName = self.inputApartmentName.text()

        if (str(street).isdigit()==True) and (str(street) is not None) and (str(street) != ""):
            
            try:
                self.pageStack.dbOperations.updateAdress(self.companyID, str(postalcode), city, street, aptName)
                print("updated")
            except Exception as err:
                print(err)
        

    def updateEmail(self):
        email = self.inputEmail.text()

        if email is not None and email != "":
            self.pageStack.dbOperations.updateEmail(self.companyID, email)
        

    def updatePhone(self):
        phone = self.inputPhone.text()

        if phone is not None and str(phone).isdigit() == True and str(phone) != "":
            self.pageStack.dbOperations.updatePhone(self.companyID, phone)

    def goback(self):
        print("go back pressed")
        
        self.pageStack.removeWidget(self)
        self.pageStack.setWindowTitle("Company Page")