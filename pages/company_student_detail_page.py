import email
from PyQt5.QtCore import Qt
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QTableWidgetItem
from PyQt5 import QtGui

from page_stack import PageStack

class CompanyStudentDetailPage(QDialog):
    def __init__(self, studentID, studentData):
        super().__init__()
        self.studentID = studentID
        self.studentData = studentData
        loadUi("ui_docs\\company_student_details.ui",self)

        self.pageStack = PageStack.getInstance()

        self.btnGoBack.clicked.connect(self.goback)

        self.showData()
        self.loadExperience()
        

    def goback(self):
        print("go back pressed")
        
        self.pageStack.removeWidget(self)
        self.pageStack.setWindowTitle("Company Page")

    def showData(self):
        self.outName.setText(self.studentData['name'])
        self.outSurname.setText(self.studentData['surname'])
        # self.outCity.setText(self.studentData['city'])
        self.outCvLink.setText(self.studentData['CVlink'])
        self.outEmail.setText(self.studentData['email'])
        self.outDepartmentName.setText(self.studentData['deptName'])
        self.outPhone.setText(self.studentData['phone'])

    def loadExperience(self):
        self.tableExperiences.setRowCount(0)

        self.tableExperiences.setColumnCount(6)
        self.tableExperiences.setHorizontalHeaderLabels(
            ('Title', 'Position', 'Start', 'End', 'Company Name', 'Company Email'))
        self.tableExperiences.setColumnWidth(0, 200)
        self.tableExperiences.setColumnWidth(1, 300)


         # show experiences in the database
        experiencesDB = self.pageStack.dbOperations.listExperience(self.studentID)

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
        