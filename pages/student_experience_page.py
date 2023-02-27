from ctypes import alignment
from PyQt5.QtCore import Qt
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5 import QtGui

from page_stack import PageStack

class StudentExperiencePage(QtWidgets.QMainWindow):
    def __init__(self, student):
        super().__init__()
        loadUi("ui_docs\\student_experience_page.ui",self)
        self.student = student

        self.pageStack = PageStack.getInstance()

        self.loadExperience()
        self.btnSave.clicked.connect(self.saveExperience)
        self.tableExperiences.doubleClicked.connect(self.doubleClick)

        self.btnGoBack.clicked.connect(self.goback)

    def goback(self):
        print("go back clicked")
        
        self.pageStack.removeWidget(self)
        self.pageStack.setWindowTitle("Student Home Page")


    def doubleClick(self):
        for item in self.ui.tableExperiences.selectedItems():
            print(item.row(), item.column(), item.text())

    def saveExperience(self):
        title = self.txtTitle.text()
        position = self.txtPosition.text()
        start = self.dateStart.date().toPyDate().strftime('%Y-%m-%d')
        end = self.dateEnd.date().toPyDate().strftime('%Y-%m-%d')
        companyName = self.txtCompanyName.text()
        companyEmail = self.txtCompanyName.text()

        #date_str = start.strftime("%d.%m.%y")

        if title and position and companyName and companyEmail is not None:

            self.pageStack.dbOperations.addExperience(self.student.userID, start, end, title, position, companyName, companyEmail)

            experiences = self.pageStack.dbOperations.listExperience(self.student.userID)

            for experience in experiences:
                # start, end, title, position, companyName, companyMail

                rowCount = self.tableExperiences.rowCount()
                print(rowCount)
                self.tableExperiences.insertRow(rowCount)
                self.tableExperiences.setItem(rowCount, 0, QTableWidgetItem(experience.title))
                self.tableExperiences.setItem(rowCount, 1, QTableWidgetItem(experience.position))
                self.tableExperiences.setItem(rowCount, 2, QTableWidgetItem(str(experience.start)))
                self.tableExperiences.setItem(rowCount, 3, QTableWidgetItem(str(experience.end)))
                self.tableExperiences.setItem(rowCount, 4, QTableWidgetItem(experience.companyName))
                self.tableExperiences.setItem(rowCount, 5, QTableWidgetItem(experience.companyMail))

    def loadExperience(self):

        experiences = [
            {'Title': 'Summer Intern', 'Position': 'Lorem Ipsum asfdf',
             'Start': '19-02-2022', 'End': '2024-06-13', 'CompanyName': 'Red Team', 'CompanyEmail': 'email@email'},
        ]

        self.tableExperiences.setRowCount(len(experiences))
        self.tableExperiences.setColumnCount(6)
        self.tableExperiences.setHorizontalHeaderLabels(
            ('Title', 'Position', 'Start', 'End', 'Company Name', 'Company Email'))
        self.tableExperiences.setColumnWidth(0, 200)
        self.tableExperiences.setColumnWidth(1, 300)

        rowIndex = 0
        for experience in experiences:
            self.tableExperiences.setItem(
                rowIndex, 0, QTableWidgetItem(experience['Title']))
            self.tableExperiences.setItem(
                rowIndex, 1, QTableWidgetItem(experience['Position']))
            self.tableExperiences.setItem(
                rowIndex, 2, QTableWidgetItem(str(experience['Start'])))
            self.tableExperiences.setItem(
                rowIndex, 3, QTableWidgetItem(str(experience['End'])))
            self.tableExperiences.setItem(
                rowIndex, 4, QTableWidgetItem(experience['CompanyName']))
            self.tableExperiences.setItem(
                rowIndex, 5, QTableWidgetItem(experience['CompanyEmail']))
            rowIndex += 1

        # show experiences in the database
        experiencesDB = self.pageStack.dbOperations.listExperience(self.student.userID)

        for experienceDB in experiencesDB:
            # start, end, title, position, companyName, companyMail
            print(experienceDB.title)

            rowCount = self.tableExperiences.rowCount()
            print(rowCount)
            self.tableExperiences.insertRow(rowCount)
            self.tableExperiences.setItem(rowCount, 0, QTableWidgetItem(experienceDB.title))
            self.tableExperiences.setItem(rowCount, 1, QTableWidgetItem(experienceDB.position))
            self.tableExperiences.setItem(rowCount, 2, QTableWidgetItem(str(experienceDB.start)))
            self.tableExperiences.setItem(rowCount, 3, QTableWidgetItem(str(experienceDB.end)))
            self.tableExperiences.setItem(rowCount, 4, QTableWidgetItem(experienceDB.companyName))
            self.tableExperiences.setItem(rowCount, 5, QTableWidgetItem(experienceDB.companyMail))
