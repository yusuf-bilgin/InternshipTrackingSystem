from ctypes import alignment
from PyQt5.QtCore import Qt
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QTableWidgetItem
from PyQt5 import QtGui
from datetime import date

from page_stack import PageStack

class InstructorAnnouncementPage(QDialog):
    def __init__(self, instructor):
        super().__init__()
        self.instructor = instructor
        loadUi("ui_docs\\instructor_publish_announcement_page.ui",self)
        self.pageStack = PageStack.getInstance()

        self.annoIDs = []

        self.tableAnnouncement.setRowCount(0)
        self.tableAnnouncement.setColumnCount(5)
        self.tableAnnouncement.setHorizontalHeaderLabels(
            ('Advisor ID', 'Announcement ID', 'Title', 'Description', 'Publish Date'))
        self.tableAnnouncement.setColumnWidth(1, 200)
        self.tableAnnouncement.setColumnWidth(2, 200)
        self.tableAnnouncement.setColumnWidth(3, 300)


        self.btnGoBack.clicked.connect(self.goback)
        self.btnAddAnnouncement.clicked.connect(self.addAnnouncement)
        self.btnDelete.clicked.connect(self.deleteAnno)
        self.listAnnouncement()

    def goback(self):
        print("go back pressed!")
        pageStack = PageStack.getInstance()
        pageStack.removeWidget(self)
        pageStack.setWindowTitle("Instructor Home Page")


    def addAnnouncement(self):

        dbops = self.pageStack.dbOperations
        print(type(date.today().strftime("%Y-%m-%d")))
        
        dbops.publishAnnouncements(self.instructor.userID,self.inputTitle.text(),self.textEdit.toPlainText(),date.today().strftime("%Y-%m-%d"))
        self.listAnnouncement()

    def listAnnouncement(self):

        dbops = self.pageStack.dbOperations
        annoList = []
        annoList = dbops.listAnnouncements(self.instructor.userID)
        self.tableAnnouncement.setRowCount(0)
        for announcement in annoList:
            rowCount = self.tableAnnouncement.rowCount()
            print(rowCount)
            self.tableAnnouncement.insertRow(rowCount)
            self.tableAnnouncement.setItem(rowCount, 0, QTableWidgetItem(str(announcement.instructor)))
            self.tableAnnouncement.setItem(rowCount, 1, QTableWidgetItem(str(announcement.idAnno)))
            self.tableAnnouncement.setItem(rowCount, 2, QTableWidgetItem(announcement.title))
            self.tableAnnouncement.setItem(rowCount, 3, QTableWidgetItem(announcement.description))
            self.tableAnnouncement.setItem(rowCount, 4, QTableWidgetItem(str(announcement.publishDate)))

            self.annoIDs.append(str(announcement.idAnno))

    def deleteAnno(self):
        print("delete working")
        idAnno = self.inputAnnoID.text()

        if self.annoIDs.count(str(idAnno))  != 0:
            print("delete inner")
            self.pageStack.dbOperations.deleteAnnouncement(self.instructor.userID, idAnno)
            self.listAnnouncement()