from urllib.parse import ParseResultBytes
from PyQt5.QtCore import Qt
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QDialogButtonBox, QVBoxLayout, QLabel, QTableWidgetItem
from PyQt5 import QtGui
from pages.company_student_detail_page import CompanyStudentDetailPage
from pages.company_profile_page import CompanyProfilePage

from page_stack import PageStack

class CompanyPage(QDialog):
    def __init__(self, company):
        super().__init__()
        self.company = company
        loadUi("ui_docs\\company_page.ui",self)

        self.pageStack = PageStack.getInstance()
        self.outCompanyName.setText("WELCOME " + self.company.cName)

        self.students = []

        self.btnSearchStudent.clicked.connect(self.searchStudent)
        self.btnGoStudentDetails.clicked.connect(self.goStudentDetails)

        self.tableStudent.setRowCount(0)
        self.tableStudent.setColumnCount(4)
        self.tableStudent.setHorizontalHeaderLabels(
            ('Student ID', 'Name', 'Surname', 'Cv link'))
        self.tableStudent.setColumnWidth(1, 200)
        self.tableStudent.setColumnWidth(2, 200)
        self.tableStudent.setColumnWidth(3, 300)



        self.btnLogout.clicked.connect(self.logout)
        self.btnGoCompanyProfile.clicked.connect(self.goProfile)
        

    def searchStudent(self):

        deptName = self.inputDepartmentName.text().upper()

        try:
            deptNo = self.pageStack.dbOperations.getDepartmentNo(str(deptName))

            if str(deptNo).isdigit()==True and str(deptNo) is not None and str(deptNo)!="" :
                students = self.pageStack.dbOperations.getAvailableStudents(deptNo)
            else:
                self.showWarning("no such department")
                raise Exception("no such department")
            self.tableStudent.setRowCount(0)
            for student in students:

                studentID = student['id']
                CVlink = student['CVlink']
                dataNameSurname = self.pageStack.dbOperations.getStudentNameSurname(studentID)
                name = dataNameSurname['name']
                surname = dataNameSurname['surname']

                rowCount = self.tableStudent.rowCount()
                print(rowCount)
                self.tableStudent.insertRow(rowCount)
                self.tableStudent.setItem(rowCount, 0, QTableWidgetItem(str(studentID)))
                self.tableStudent.setItem(rowCount, 1, QTableWidgetItem(name))
                self.tableStudent.setItem(rowCount, 2, QTableWidgetItem(surname))
                self.tableStudent.setItem(rowCount, 3, QTableWidgetItem(CVlink))

                
                # city = self.pageStack.dbOperations.getStudentCity(studentID)

                mailPhone = self.pageStack.dbOperations.getStudentMailPhone(studentID)
                email = mailPhone['email']
                phone = mailPhone['phone']

                studentInfo = {'id': studentID, 'name': name, 'surname': surname, 'city': 'none', 'CVlink': CVlink,
                             'email': email, 'deptName': deptName, 'phone': phone}

                self.students.append(studentInfo)
                


        except Exception as err:
            self.showWarning(str(err))
            print(err, "ERROR")
        

    def goStudentDetails(self):
        print("go student details presed")
        # TODO validate student id: studentIDs = []
        enteredID = self.inputStudentID.text()
        
        if (enteredID is not None) and (enteredID != "") and (enteredID.isdigit()==True):
            isvalid = False
            index = 0

            for studentInfos in self.students:
                if str(studentInfos['id']) == enteredID:
                    isvalid = True
                    print("EŞLEŞTİ")
                    break
                index += 1

            if isvalid:
                companyStudentDetailPage = CompanyStudentDetailPage(enteredID, self.students[index])
        
                self.pageStack.addWidget(companyStudentDetailPage)
                self.pageStack.setWindowTitle("Student Details")
                self.pageStack.setCurrentIndex(self.pageStack.currentIndex()+1)
            else:
                print("İÇ")
        else:
                print("DIŞ")

    def logout(self):
        print("Logout pressed")
        self.pageStack.removeWidget(self)
        self.pageStack.setWindowTitle("Login Page")

    def goProfile(self):
        print("go profile presed")
        companyProfilePage = CompanyProfilePage(self.company.userID)
        self.pageStack.addWidget(companyProfilePage)
        self.pageStack.setWindowTitle("Company Profile Update")
        self.pageStack.setCurrentIndex(self.pageStack.currentIndex()+1)

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