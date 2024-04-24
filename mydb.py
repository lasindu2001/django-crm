import mysql.connector

dataBase = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='root123',
    auth_plugin='mysql_native_password'  
)

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE IF NOT EXISTS elderco")

dataBase = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='root123',
    database='elderco',  
    auth_plugin='mysql_native_password'  
)

cursorObject = dataBase.cursor()

print("All done")