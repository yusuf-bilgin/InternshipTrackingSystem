from PyQt5.QtCore import Qt
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QTableWidgetItem, QDialogButtonBox, QVBoxLayout, QLabel
from PyQt5 import QtGui

from page_stack import PageStack

class StudentProfilePage(QDialog):
    def __init__(self, student):
        super().__init__()
        loadUi("ui_docs\\student_profile_page.ui",self)
        self.student = student

        self.possibleIDs = []

        self.pageStack = PageStack.getInstance()

        self.tableInstructors.setRowCount(0)
        self.tableInstructors.setColumnCount(5)
        self.tableInstructors.setHorizontalHeaderLabels(('Instructor id', 'Name', 'Surname', 'Email', 'Phone'))
        self.showInstructors()

        self.btnGoBack.clicked.connect(self.goback)
        self.currentAdvisor.setText("Current Advisor ID: " + self.pageStack.dbOperations.getAdvisorID(self.student.userID))
        self.currentCV.setText("Current CV link: " + self.pageStack.dbOperations.getCVlink(self.student.userID))
        self.btnUpdateAdvisor.clicked.connect(self.updateAdvisor)
        self.btnUpdateCVlink.clicked.connect(self.updateCVlink)
        

    def showInstructors(self):
        instructors = self.pageStack.dbOperations.getInstructorsFromDepartment(self.student.deptNo)

        for instructorData in instructors:
            # instructor = {'id': row[0], 'name':row[1], 'surname':row[2], 'email':'aaasd', 'phone':'2105'}
            rowCount = self.tableInstructors.rowCount()
            print(rowCount)
            self.tableInstructors.insertRow(rowCount)
            self.tableInstructors.setItem(rowCount, 0, QTableWidgetItem(str(instructorData['id'])))
            self.tableInstructors.setItem(rowCount, 1, QTableWidgetItem(instructorData['name']))
            self.tableInstructors.setItem(rowCount, 2, QTableWidgetItem(instructorData['surname']))
            self.tableInstructors.setItem(rowCount, 3, QTableWidgetItem(instructorData['email']))
            self.tableInstructors.setItem(rowCount, 4, QTableWidgetItem(instructorData['phone']))

            self.possibleIDs.append(str(instructorData['id']))

    def updateAdvisor(self):
        chosenAdvisorID = self.inputAdvisorID.text()
        
        if(chosenAdvisorID is not None and chosenAdvisorID!="") and (chosenAdvisorID.isdigit() == True) and ( self.possibleIDs.count(chosenAdvisorID) != 0):
            self.pageStack.dbOperations.setAdvisor(self.student.userID, chosenAdvisorID)
            self.currentAdvisor.setText("Current Advisor ID: " + self.pageStack.dbOperations.getAdvisorID(self.student.userID))
            self.showWarning("updated")
        else:
            self.showWarning("Entered advisor id must be a positive integer."
            "\nId must be chosen from the list."
            "\nDo not leave the input field empty.")

    def updateCVlink(self):
        enteredLink = self.inputCVlink.text()
        if (enteredLink is not None) and (enteredLink!=""):
            self.pageStack.dbOperations.addCVlink(self.student.userID, enteredLink)
            self.currentCV.setText("Current CV link: " + self.pageStack.dbOperations.getCVlink(self.student.userID))
            self.showWarning("CV link updated")
        else:
            self.showWarning("Do not leave the the input field empty!")


    def goback(self):
        print("go back pressed")
        
        self.pageStack.removeWidget(self)
        self.pageStack.setWindowTitle("Student Home Page")

    def showWarning(self, text):
        dlg = CustomDialog(text)
        if dlg.exec():
            print("Success!")
        else:
            print("Cancel!")

class CustomDialog(QDialog):
    def __init__(self, text, parent=None):
        super().__init__(parent)


        if text=="updated":
            self.setWindowTitle("CONGRATS :)")

            QBtn = QDialogButtonBox.Ok

            self.buttonBox = QDialogButtonBox(QBtn)
            self.buttonBox.accepted.connect(self.accept)

            self.layout = QVBoxLayout()
            message = QLabel("Advisor is succesfully updated :)")
            self.layout.addWidget(message)
            self.layout.addWidget(self.buttonBox)
            self.setLayout(self.layout)

        else:
            self.setWindowTitle("Warning!")

            QBtn = QDialogButtonBox.Ok

            self.buttonBox = QDialogButtonBox(QBtn)
            self.buttonBox.accepted.connect(self.accept)

            self.layout = QVBoxLayout()
            message = QLabel(text)
            self.layout.addWidget(message)
            self.layout.addWidget(self.buttonBox)
            self.setLayout(self.layout)