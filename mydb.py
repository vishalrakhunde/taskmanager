import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user ='root',
    passwd='vishal06'
)

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE taskmanagerdb")

print("All Done!")