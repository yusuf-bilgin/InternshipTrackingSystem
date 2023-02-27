from PyQt5.QtWidgets import QStackedWidget

from database_operations import DatabaseOperations

class PageStack(QStackedWidget):
    __instance = None

    @staticmethod 
    def getInstance():
        """ Static access method. """
        if PageStack.__instance == None:
            PageStack()
        return PageStack.__instance

    def __init__(self):
        """ Virtually private constructor. """
        if PageStack.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            super().__init__()
            self.dbOperations = DatabaseOperations()
            PageStack.__instance = self