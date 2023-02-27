from ctypes import alignment
from PyQt5.QtCore import Qt
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QDialogButtonBox, QVBoxLayout, QLabel, QTableWidgetItem
from PyQt5 import QtGui
from pages.instructor_profile_page import InstructorProfilePage

from page_stack import PageStack

class InstructorApprovalPage(QDialog):
    def __init__(self, instructor):
        super().__init__()
        self.instructor = instructor
        loadUi("ui_docs\\instructor_approval_page.ui",self)
        self.docIDs = []
        self.pageStack = PageStack.getInstance()

        self.tableDocument.setRowCount(0)
        self.tableDocument.setColumnCount(5)
        self.tableDocument.setHorizontalHeaderLabels(
            ('Student ID', 'Document ID', 'Title', 'Link', 'Approval Status'))
        self.tableDocument.setColumnWidth(2, 150)
        self.tableDocument.setColumnWidth(3, 300)
        self.tableDocument.setColumnWidth(4, 150)

        
        self.btnGoBack.clicked.connect(self.goback)
        self.btnApprove.clicked.connect(self.approveDoc)
        self.btnDisapprove.clicked.connect(self.disapproveDoc)
        # self.btnListDocuments.clicked.connect(self.listDocs)
        

        # self.btnProfile.clicked.connect(self.goProfile)

        self.listDocs()

    def goProfile(self):
        print("go profile pressed!")
        pageStack = PageStack.getInstance()
        pageStack.addWidget(InstructorProfilePage(self.instructor))
        pageStack.setWindowTitle("Instructor Home Page")

    def goback(self):
        print("go back pressed!")
        pageStack = PageStack.getInstance()
        pageStack.removeWidget(self)
        pageStack.setWindowTitle("Instructor Home Page")


    def approveDoc(self):

        if self.checkIsnumericAndExist():
            dbops = self.pageStack.dbOperations

            dbops.approveDocs(self.inputDocID.text())#kullanıcının girdiği doc id buraya parametre olarak gitcek
            self.showWarning("Document is approved!")
            self.listDocs()


    def disapproveDoc(self):
        
        if self.checkIsnumericAndExist():
            dbops = self.pageStack.dbOperations

            dbops.disapproveDocs(self.inputDocID.text())#kullanıcının girdiği doc id buraya parametre olarak gitcek
            self.listDocs()
            self.showWarning("Document is disapproved!")
            

    def listDocs(self):

        dbops = self.pageStack.dbOperations

        docList = dbops.listDocs(self.instructor.userID)
        self.tableDocument.setRowCount(0)
        for doc in docList:
            # IDstudent, docID, docTitle, link, approvalStatus

            rowCount = self.tableDocument.rowCount()
            print(rowCount)
            self.tableDocument.insertRow(rowCount)

            self.tableDocument.setItem(rowCount, 0, QTableWidgetItem(str(doc.IDstudent)))
            self.tableDocument.setItem(rowCount, 1, QTableWidgetItem(str(doc.docID)))
            self.tableDocument.setItem(rowCount, 2, QTableWidgetItem(doc.docTitle))
            self.tableDocument.setItem(rowCount, 3, QTableWidgetItem(doc.link))
            self.tableDocument.setItem(rowCount, 4, QTableWidgetItem(doc.approvalStatus))

            self.docIDs.append(str(doc.docID))

        #list the docs lol
    def checkIsnumericAndExist(self):
        enteredID = self.inputDocID.text()
        if (enteredID is not None and enteredID!="") and (enteredID.isdigit() == True) and ( self.docIDs.count(enteredID) != 0):
            return True

        self.showWarning("Document id must be numeric!\nDocumetn id must be chosen from the list")

        return False

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