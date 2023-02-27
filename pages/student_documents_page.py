from ctypes import alignment
from PyQt5.QtCore import Qt
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QTableWidgetItem
from PyQt5 import QtGui

from page_stack import PageStack

class StudentDocumentsPage(QDialog):
    def __init__(self, student):
        super().__init__()
        loadUi("ui_docs\\student_documents.ui",self)
        self.student = student
        self.pageStack = PageStack.getInstance()


        self.widgetStack.addWidget(self.documents)
        self.widgetStack.addWidget(self.addDocumentPage)

        self.tableDocument.setRowCount(0)
        self.tableDocument.setColumnCount(4)
        self.tableDocument.setHorizontalHeaderLabels(
            ('Doc ID', 'Doc Title', 'Link', 'Approval Status'))
        self.tableDocument.setColumnWidth(1, 200)
        self.tableDocument.setColumnWidth(2, 300)
        self.tableDocument.setColumnWidth(3, 200)


        self.btnListDocuments.clicked.connect(self.displayDocuments)
        self.btnAddDocuments.clicked.connect(self.displayAddDocuments)
        self.btnAdd.clicked.connect(self.addDocument)
        self.btnGoback.clicked.connect(self.goBack)

    def displayDocuments(self):

        documents = self.pageStack.dbOperations.listDocuments(self.student.userID)
        self.tableDocument.setRowCount(0)
        for doc in documents:
            # IDstudent, docID, docTitle, link, approvalStatus

            rowCount = self.tableDocument.rowCount()
            print(rowCount)
            self.tableDocument.insertRow(rowCount)
            self.tableDocument.setItem(rowCount, 0, QTableWidgetItem(str(doc.docID)))
            self.tableDocument.setItem(rowCount, 1, QTableWidgetItem(doc.docTitle))
            self.tableDocument.setItem(rowCount, 2, QTableWidgetItem(doc.link))
            self.tableDocument.setItem(rowCount, 3, QTableWidgetItem(doc.approvalStatus))


        self.widgetStack.setCurrentIndex(0)

    def displayAddDocuments(self):
        self.widgetStack.setCurrentIndex(1)

    def addDocument(self):
        title = self.inputTitle.text()
        link = self.inputLink.text()

        if (title is not None and title != "") and (link is not None and link != ""):
            self.pageStack.dbOperations.addStudentDocs(self.student.userID, title, link)

    def goBack(self):
        print("go back clicked")
        
        self.pageStack.removeWidget(self)
        self.pageStack.setWindowTitle("Student Home Page")

