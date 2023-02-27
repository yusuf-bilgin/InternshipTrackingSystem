

from sqlite3 import connect
from mysql.connector import errorcode 
import mysql.connector
from experience import Experience
from document import Document
from announcement import Announcement
from company import Company
from instructor import Instructor
from student import Student
from dbHelper import DbHelper
from user import User
        
class DatabaseOperations():
    def __init__(self):
        self.dbHelper = DbHelper()

    def insertUser(self, userName, password, phone, email):
        try:
            connection = self.dbHelper.getConnection()
            cursor = connection.cursor()

            queryInsertUser = ("INSERT INTO user "
                                "(userName, password, phone, email) "
                                "VALUES (%s, md5(%s), %s, %s)")

            dataUser = (userName, password, phone, email)

            cursor.execute(queryInsertUser, dataUser)

            connection.commit()
            cursor.close()
            connection.close()

        except Exception as err:
            raise err

    def insertPerson(self, personID, name, surname, gender):
        try:
            connection = self.dbHelper.getConnection()
            cursor = connection.cursor()

            queryInsertPerson = ("INSERT INTO person "
                                "(personID, name, surname, gender) "
                                "VALUES (%s, %s, %s, %s)")

            dataPerson = (personID, name, surname, gender)

            cursor.execute(queryInsertPerson, dataPerson)

            connection.commit()
            cursor.close()
            connection.close()

        except Exception as err:
            raise err

    def insertStudent(self, studentID, deptNo, birthdate, age, jobStatus):
        try:
            connection = self.dbHelper.getConnection()
            cursor = connection.cursor()

            queryInsertStudent = ("INSERT INTO student "
                            "(studentID, deptNo, birthdate, age, jobStatus) "
                            "VALUES (%s, %s, %s, %s, %s)")

            dataStudent = (studentID, deptNo, birthdate, age, jobStatus)

            cursor.execute(queryInsertStudent, dataStudent)

            connection.commit()
            cursor.close()
            connection.close()
            
        except Exception as err:
            raise err

    
    def insertInstructor(self, instructorID, deptNo):
        try:
            connection = self.dbHelper.getConnection()
            cursor = connection.cursor()

            queryInsertStudent = ("INSERT INTO instructor "
                            "(instructorID, deptNo) "
                            "VALUES (%s, %s)")

            dataStudent = (instructorID, deptNo)

            cursor.execute(queryInsertStudent, dataStudent)

            connection.commit()
            cursor.close()
            connection.close()
            
        except Exception as err:
            raise err

    def insertCompany(self, companyID, cName):
        try:
            connection = self.dbHelper.getConnection()
            cursor = connection.cursor()

            queryInsertCompany = ("INSERT INTO company "
                            "(companyID, cName) "
                            "VALUES (%s, %s)")

            dataCompany = (companyID, cName)

            cursor.execute(queryInsertCompany, dataCompany)

            connection.commit()
            cursor.close()
            connection.close()
            
        except Exception as err:
            raise err
        
    def getUserID(self, userName, password):
        try:
            connection = self.dbHelper.getConnection()
            cursor = connection.cursor()

            queryGetID = ("SELECT userID from user "
                            "WHERE username = %s AND password = md5(%s)")
            
            dataUser = (userName, password)

            cursor.execute(queryGetID, dataUser)

            uid = cursor.fetchone()[0]

            cursor.close()
            connection.close()

            return uid
            
        except  mysql.connector.Error as err:
            if err.errno == errorcode.CR_NO_RESULT_SET:
                raise Exception("Something went wrong. Try again.") # girilen bilgiyle eşleşen user yok
            else:
                raise err

    def getDepartmentNo(self, deptName):
        try:
            connection = self.dbHelper.getConnection()
            cursor = connection.cursor()

            queryGetDeptNo = ("SELECT deptNo from department "
                            "WHERE deptName = %s")
            
            dataStudent = (deptName,)

            cursor.execute(queryGetDeptNo, dataStudent)

            row = cursor.fetchone()
            deptNo = row[0]

            cursor.close()
            connection.close()

            return deptNo
            
        except  mysql.connector.Error as err:
            if err.errno == errorcode.CR_NO_RESULT_SET:
                raise Exception("Something went wrong. Try again.") # girilen bilgiyle eşleşen user yok
            else:
                raise err

    def doesUserExist(self, username, password):
        try:
            connection = self.dbHelper.getConnection()
            cursor = connection.cursor()

            queryGetUserID = ("SELECT count(*), userID from user "
                            "WHERE userName = %s AND password =md5(%s)")
            
            dataStudent = (username, password)

            cursor.execute(queryGetUserID, dataStudent)

            
            row = cursor.fetchone()
            count = row[0]
            uid = row[1]

            cursor.close()
            connection.close()

            if count == 1:
                return uid
            else:
                return -1
            
        except  mysql.connector.Error as err:
            if err.errno == errorcode.CR_NO_RESULT_SET:
                raise Exception("Something went wrong. Try again.") # girilen bilgiyle eşleşen user yok
            else:
                raise err

    def getUserData(self, uid):
        try:
            connection = self.dbHelper.getConnection()
            cursor = connection.cursor()

            queryGetUserData = ("SELECT * from user "
                            "WHERE userID = %s")
            
            data = (uid,)

            cursor.execute(queryGetUserData, data)

            
            row = cursor.fetchone()

            username = row[1]
            password = row[2]
            phone = row[3]
            email = row[4]
            
            dataUser = {
                'username':username,
                'password':password,
                'phone':phone,
                'email':email,
            }

            cursor.close()
            connection.close()
            return dataUser
            
        except  mysql.connector.Error as err:
            if err.errno == errorcode.CR_NO_RESULT_SET:
                raise Exception("Something went wrong. Try again.") # girilen bilgiyle eşleşen user yok
            else:
                raise err

    def getPersonData(self, uid):
        try:
            connection = self.dbHelper.getConnection()
            cursor = connection.cursor()

            queryGetPersonData = ("SELECT * from person "
                            "WHERE personID = %s")
            
            data = (uid,)

            cursor.execute(queryGetPersonData, data)

            
            row = cursor.fetchone()

            name = row[1]
            surname = row[2]
            gender = row[3]
            
            dataPerson = {
                'name':name,
                'surname':surname,
                'gender':gender,
            }

            cursor.close()
            connection.close()
            return dataPerson
            
        except  mysql.connector.Error as err:
            if err.errno == errorcode.CR_NO_RESULT_SET:
                raise Exception("Something went wrong. Try again.") # girilen bilgiyle eşleşen user yok
            else:
                raise err

    def getInstructor(self, uid):
        try:
            userData = self.getUserData(uid)
            personData = self.getPersonData(uid)

            userName = userData['username']
            password = userData['password']
            phone = userData['phone']
            email = userData['email']

            name = personData['name']
            surname = personData['surname']
            gender = personData['gender']

            connection = self.dbHelper.getConnection()
            cursor = connection.cursor()

            queryGetInstructorData = ("SELECT * from instructor "
                            "WHERE instructorID = %s")
            
            data = (uid,)

            cursor.execute(queryGetInstructorData, data)

            row = cursor.fetchone()

            deptNo = row[1]
            

            instructor = Instructor(uid, password, userName, phone, email, name, surname, gender, deptNo)

            cursor.close()
            connection.close()
            return instructor
            
        except  mysql.connector.Error as err:
            if err.errno == errorcode.CR_NO_RESULT_SET:
                raise Exception("Something went wrong. Try again.") # girilen bilgiyle eşleşen user yok
            else:
                raise err

    def getStudent(self, uid):
        try:

            userData = self.getUserData(uid)
            personData = self.getPersonData(uid)

            userName = userData['username']
            password = userData['password']
            phone = userData['phone']
            email = userData['email']

            name = personData['name']
            surname = personData['surname']
            gender = personData['gender']

            connection = self.dbHelper.getConnection()
            cursor = connection.cursor()

            queryGetStudentData = ("SELECT * from student "
                            "WHERE studentID = %s")
            
            dataStudent = (uid,)

            cursor.execute(queryGetStudentData, dataStudent)

            
            row = cursor.fetchone()
            deptNo = row[1]
            birthdate = row[2]
            age = row[3]
            jobStatus = row[4]
            advisorID = row[5]
            CVlink = row[6]

            student = Student(uid, userName, password, phone, email, name, surname, gender, 
                            birthdate, age, jobStatus, deptNo, advisorID, CVlink)

            cursor.close()
            connection.close()

            return student
            
            
        except  mysql.connector.Error as err:
            if err.errno == errorcode.CR_NO_RESULT_SET:
                raise Exception("Something went wrong. Try again.") # girilen bilgiyle eşleşen user yok
            else:
                raise err

    def getCompany(self, uid):
        try:
            userData = self.getUserData(uid)

            userName = userData['username']
            password = userData['password']
            phone = userData['phone']
            email = userData['email']

            connection = self.dbHelper.getConnection()
            cursor = connection.cursor()

            queryGetCompanyData = ("SELECT * from company "
                            "WHERE companyID = %s")
            
            data = (uid,)

            cursor.execute(queryGetCompanyData, data)

            
            row = cursor.fetchone()
            cName = row[1]

            company = Company(uid, password, userName, phone, email, cName)

            cursor.close()
            connection.close()

            return company
            
            
        except  mysql.connector.Error as err:
            if err.errno == errorcode.CR_NO_RESULT_SET:
                raise Exception("Something went wrong. Try again.") # girilen bilgiyle eşleşen user yok
            else:
                raise err

    def getAllUsers(self):
        try:
            connection = self.dbHelper.getConnection()

            cursor = connection.cursor()

            query2 = ("SELECT * FROM internship.user")

            cursor.execute(query2)

            #users = []

            # for (userID, userName, password, phone, email) in cursor:
            #     print("userID is: {}, username is: {}, password is: {}, phone is: {}, email is: {}".format(
            #         userID, userName, password, phone, email))

            #     users.append(userName)

            # print("\n")

            users = []

            for row in cursor:
                user = User(row[0], row[1], row[2], row[3], row[4])
                users.append(user)

            for user in users:
                print(user.userName)

            cursor.close()
            connection.close()

            return users

        except Exception as err:
            raise err

    def addStudentDocs(self, IDstudent, docTitle, link):

        connection = self.dbHelper.getConnection()
        cursor = connection.cursor()

        query = "INSERT INTO document(IDstudent, docTitle, link, approvalStatus) VALUES(%s, %s, %s, %s)"
        values = (IDstudent, docTitle, link, "none")  # Will be taken as input

        cursor.execute(query, values)
        try:
            connection.commit()
            print(f'{cursor.rowcount} records added succesfully!')
            print(f'ID of the last record: {cursor.lastrowid}')
        except Exception as err:
            raise err

    def listDocuments(self, IDstudent):
        try:
            connection = self.dbHelper.getConnection()
            cursor = connection.cursor()

            query = ("SELECT * FROM document WHERE IDstudent = %s")
            querydata = (IDstudent,)
            cursor.execute(query, querydata)

            documents = []

            for row in cursor:
                document = Document(row[0], row[1], row[2], row[3], row[4])
                documents.append(document)

            for document in documents:
                print(document.docTitle, document.link)

            cursor.close()
            connection.close()

            return documents

        except Exception as err:
            raise err

    def listAnnouncements(self, instructorID):

        try:
            connection = self.dbHelper.getConnection()
            cursor = connection.cursor()

            query = ("SELECT * FROM announcement WHERE instructor = %s")
            querydata = (instructorID,)

            cursor.execute(query, querydata)

            announcements = []

            for row in cursor:
                announcement = Announcement(
                    row[0], row[1], row[2], row[3], row[4])
                announcements.append(announcement)

            # for announcement in announcements:
            #     print(announcement.title, announcement.description)

            cursor.close()
            connection.close()

            return announcements

        except Exception as err:
            raise err

    def publishAnnouncements(self,instID,annoTitle,annoDesc,currentDate):
        try:
            connection = self.dbHelper.getConnection()

            cursor = connection.cursor()

            queryPA = ("INSERT INTO announcement (instructor, title, description, publishDate) VALUES (%s, %s, %s, %s)")
            querydata = (instID, annoTitle, annoDesc, currentDate)

            cursor.execute(queryPA, querydata)

            connection.commit()

            cursor.close()
            connection.close()

        except Exception as err:
            raise err


    def addExperience(self, studentID, start, end, title, position, companyName, companyMail):
        try:
            connection = self.dbHelper.getConnection()
            cursor = connection.cursor()

            query = ("INSERT INTO experience(student, start, end, title, position, companyName, companyMail) VALUES(%s,%s,%s,%s,%s,%s, %s)")
            values = (studentID, start, end, title, position, companyName, companyMail)
            cursor.execute(query, values)

            connection.commit()
            cursor.close()
            connection.close()

        except Exception as err:
            print(err)


    def listExperience(self, studentID):
        try:
            connection = self.dbHelper.getConnection()
            cursor = connection.cursor()

            query = ("SELECT * FROM experience WHERE student = %s")
            querydata = (studentID,)

            cursor.execute(query, querydata)

            experiences = []

            for row in cursor:
                experience = Experience(
                    row[0], row[1], row[2], row[3], row[4], row[5], row[6])
                experiences.append(experience)

            cursor.close()
            connection.close()

            return experiences

        except Exception as err:
            raise err

    def approveDocs(self,docID):
        try:
            connection = self.dbHelper.getConnection()

            cursor = connection.cursor()

            queryAD = ("UPDATE document SET approvalStatus = 'yes' WHERE docID = %s")
            querydata = (docID,)

            cursor.execute(queryAD, querydata)

            connection.commit()

            cursor.close()
            connection.close()


        except Exception as err:
            raise err



    def disapproveDocs(self,docID):
        try:

            connection = self.dbHelper.getConnection()

            cursor = connection.cursor()

            queryDD = ("UPDATE document SET approvalStatus = 'no' WHERE docID = %s")
            querydata = (docID,)

            cursor.execute(queryDD, querydata)

            connection.commit()

            cursor.close()
            connection.close()
        
        except Exception as err:
            raise err

    def listDocs(self, instructorID):

        try:

            connection = self.dbHelper.getConnection()

            cursor = connection.cursor()

            querystudentID = ("SELECT studentID FROM student WHERE advisorID = %s")
            querydata1 = (instructorID,)

            cursor.execute(querystudentID, querydata1)
            studentIDs = cursor.fetchall()
            docList = []
            for studentID in studentIDs:
                queryLD = ("SELECT * FROM document WHERE IDstudent = %s")
                querydata2 = (studentID[0],)
                cursor.execute(queryLD, querydata2)
                rows = cursor.fetchall()

                for row in rows:
                    doc = Document(row[0], row[1], row[2], row[3], row[4])
                    docList.append(doc)

            cursor.close()
            connection.close()

            return docList

        except Exception as err:
            raise err

    def getStudentNameSurname(self, studentID):
        try:
            connection = self.dbHelper.getConnection()

            cursor = connection.cursor()

            query = ("SELECT name, surname FROM person WHERE personID=%s")
            querydata = (studentID,)
            cursor.execute(query, querydata)

            row = cursor.fetchone()

            data = {'name': row[0],
                    'surname': row[1]
                }
                


            cursor.close()
            connection.close()

            return data

        except Exception as err:
            raise err




    def getStudentMailPhone(self, studentID):
        try:
            connection = self.dbHelper.getConnection()

            cursor = connection.cursor()

            query = ("SELECT email, phone FROM user WHERE userID=%s")
            querydata = (studentID,)
            cursor.execute(query, querydata)


            row = cursor.fetchone()

            data = {'email': row[0], 'phone': row[1]}
                


            cursor.close()
            connection.close()

            return data

        except Exception as err:
            raise err



    def getStudentCity(self, studentID):
        try:
            connection = self.dbHelper.getConnection()

            cursor = connection.cursor()

            query = ("SELECT city FROM address WHERE userID=%s")
            querydata = (studentID,)

            cursor.execute(query, querydata)


            city = cursor.fetchone()[0]

            cursor.close()
            connection.close()

            return city

        except Exception as err:
            raise err




    def getAvailableStudents(self, deptNo):
        try:
            connection = self.dbHelper.getConnection()

            cursor = connection.cursor()

            query = ("SELECT studentID, CVlink FROM student WHERE jobStatus= %s AND deptNo = %s")
            querydata = ("no", deptNo)

            cursor.execute(query, querydata)

            rows = cursor.fetchall()

            students = []

            for row in rows:
                studentData = {'id': row[0], 'CVlink':row[1]}
                students.append(studentData)

            cursor.close()
            connection.close()

            return students

        except Exception as err:
            raise err


    def getInstructorsFromDepartment(self, deptNo):
        try:
            connection = self.dbHelper.getConnection()

            cursor = connection.cursor()

            query = ("select personID, name, surname from person right join "
            "(select distinct(instructorID) from instructor where instructor.deptNo = %s) as inst "
            "on inst.instructorID = personID")

            querydata = (deptNo,)

            cursor.execute(query, querydata)

            instructors = []

            for row in cursor:
                instructor = {'id': row[0], 'name':row[1], 'surname':row[2], 'email':'none', 'phone':'none'}
                instructors.append(instructor)

            query2 = ("select email, phone from user right join "
            "(select distinct(instructorID) from instructor where instructor.deptNo = %s) as inst "
            "on user.userID = inst.instructorID")

            querydata2 = (deptNo,)

            cursor.execute(query2, querydata2)

            index = 0
            for row in cursor:
                inst = instructors[index]
                inst['email'] = row[0]
                inst['phone'] = row[1]
                index += 1


            cursor.close()
            connection.close()

            return instructors

        except Exception as err:
            raise err

    def setAdvisor(self, studentID, instructorID):
        try:
            connection = self.dbHelper.getConnection()

            cursor = connection.cursor()

            query = ("UPDATE student SET advisorID = %s WHERE studentID = %s")

            querydata = (instructorID, studentID)

            cursor.execute(query, querydata)

            connection.commit()

            cursor.close()
            connection.close()

        except Exception as err:
            raise err

    def addCVlink(self, studentID, link):
        try:
            connection = self.dbHelper.getConnection()

            cursor = connection.cursor()

            query = ("UPDATE student SET CVlink = %s WHERE studentID = %s")

            querydata = (link, studentID)

            cursor.execute(query, querydata)

            connection.commit()

            cursor.close()
            connection.close()

        except Exception as err:
            raise err     

    def getAdvisorID(self, studentID):
        try:
            connection = self.dbHelper.getConnection()

            cursor = connection.cursor()

            query = ("SELECT advisorID from student WHERE studentID = %s")

            querydata = (studentID,)

            cursor.execute(query, querydata)

            advisorID = cursor.fetchone()

            cursor.close()
            connection.close()

            if advisorID is not None:
                return str(advisorID[0])
            else:
                return 'none'

        except Exception as err:
            raise err 

    def getCVlink(self, studentID):
        try:
            connection = self.dbHelper.getConnection()

            cursor = connection.cursor()

            query = ("SELECT CVlink from student WHERE studentID = %s")

            querydata = (studentID,)

            cursor.execute(query, querydata)

            CVlink = cursor.fetchone()

            cursor.close()
            connection.close()

            if CVlink is not None:
                return str(CVlink[0])
            else:
                return 'none'

        except Exception as err:
            raise err

    def deleteAnnouncement(self, instructorID, idAnno):
        try:
            connection = self.dbHelper.getConnection()

            cursor = connection.cursor()

            query = ("DELETE from announcement where instructor = %s AND idAnno = %s")

            querydata = (instructorID, idAnno)

            cursor.execute(query, querydata)

            connection.commit()
            cursor.close()
            connection.close()

        except Exception as err:
            raise err

    def updateAdress(self, userID, postalcode, city, street, aptName):
        try:
            connection = self.dbHelper.getConnection()

            cursor = connection.cursor()

            query = ("update address set postalcode = %s, city = %s, street = %s, aptName = %s where userID = %s")

            querydata = (postalcode, city, street, aptName, userID)

            cursor.execute(query, querydata)

            connection.commit()
            
            cursor.close()
            connection.close()

        except Exception as err:
            raise err
        

    def updateEmail(self, userID, email):
        try:
            connection = self.dbHelper.getConnection()

            cursor = connection.cursor()

            query = ("update user set email = %s where userID = %s")

            querydata = (email, userID)

            cursor.execute(query, querydata)

            connection.commit()
            cursor.close()
            connection.close()

        except Exception as err:
            raise err
        

    def updatePhone(self, userID, phone):
        try:
            connection = self.dbHelper.getConnection()

            cursor = connection.cursor()

            query = ("update user set phone = %s where userID = %s")

            querydata = (phone, userID)

            cursor.execute(query, querydata)

            connection.commit()
            cursor.close()
            connection.close()

        except Exception as err:
            raise err
        

