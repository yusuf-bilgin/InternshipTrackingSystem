from ctypes import alignment
from PyQt5.QtCore import Qt
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QTableWidgetItem
from PyQt5 import QtGui

from page_stack import PageStack

class StudentAnnouncementPage(QDialog):
    def __init__(self, student):
        super().__init__()
        loadUi("ui_docs\\student_announcement.ui",self)
        self.student = student
        self.pageStack = PageStack.getInstance()

        self.tableAnnouncement.setRowCount(0)
        self.tableAnnouncement.setColumnCount(5)
        self.tableAnnouncement.setHorizontalHeaderLabels(
            ('Advisor ID', 'Announcement ID', 'Title', 'Description', 'Publish Date'))
        self.tableAnnouncement.setColumnWidth(1, 200)
        self.tableAnnouncement.setColumnWidth(2, 200)
        self.tableAnnouncement.setColumnWidth(3, 300)

        self.showAnnouncements()

        self.btnGoBack.clicked.connect(self.goback)

    def goback(self):
        print("go back pressed!")
        
        self.pageStack.removeWidget(self)
        self.pageStack.setWindowTitle("Student Home Page")

    def showAnnouncements(self):
        advisorID = self.pageStack.dbOperations.getAdvisorID(self.student.userID)

        if(advisorID is not None) and (advisorID != ""):
            # show announcements
            announcements = self.pageStack.dbOperations.listAnnouncements(advisorID)

            for announcement in announcements:
                # instructor, idAnno, title, description, publishDate

                rowCount = self.tableAnnouncement.rowCount()
                print(rowCount)
                self.tableAnnouncement.insertRow(rowCount)
                self.tableAnnouncement.setItem(rowCount, 0, QTableWidgetItem(str(announcement.instructor)))
                self.tableAnnouncement.setItem(rowCount, 1, QTableWidgetItem(str(announcement.idAnno)))
                self.tableAnnouncement.setItem(rowCount, 2, QTableWidgetItem(announcement.title))
                self.tableAnnouncement.setItem(rowCount, 3, QTableWidgetItem(announcement.description))
                self.tableAnnouncement.setItem(rowCount, 4, QTableWidgetItem(str(announcement.publishDate)))
