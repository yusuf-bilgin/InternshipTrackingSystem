import mysql.connector

class DbHelper():
    def __init__(self):
        self.host = "localhost"
        self.user = "root"
        self.password = "PdqYWRqw5n"
        self.database = 'internship'
        
    def getConnection(self):

        connection = mysql.connector.connect(host = "localhost",
                                    user='root', 
                                    password = "PdqYWRqw5n",
                                    database='internship', )
        return connection

