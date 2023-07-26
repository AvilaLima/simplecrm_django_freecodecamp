import mysql.connector

dataBase = mysql.connector.connect(
    host = '192.168.8.7',
    user = 'alexandre',
    passwd = 'sppe@123'
)

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE elderco")

print ("Banco de dados criado com sucesso")