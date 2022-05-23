import mysql.connector

class DbHelper:
    mydb = None
    def __init__(self) -> None:
        self.__mycursor = None


    def get_cursor(self):
        if DbHelper.mydb == None:
            DbHelper.mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="root",
                database="banking_db"
            )
            self.__mycursor = DbHelper.mydb.cursor()
        else:
            self.__mycursor = DbHelper.mydb.cursor()
        return self.__mycursor
