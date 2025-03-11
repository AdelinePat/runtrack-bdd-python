import sys
# from sys.path["C:\Users\Adeline\Documents\Projetdev\constants_info.py"] import PASSWORD
# from ....Projetdev import constants_info
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password= "",
    database="LaPlateforme"
)

if mydb.is_connected():
    db_info = mydb.get_server_info()
    print(f" Connecté à MySQL, version : {db_info}")

    cursor = mydb.cursor()
    cursor.execute("SELECT DATABASE();")
    db_name = cursor.fetchone()

    cursor.close()

mydb.close()