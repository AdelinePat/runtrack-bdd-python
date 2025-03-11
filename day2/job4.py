import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password= "",
    database="LaPlateforme"
)

if mydb.is_connected():
    
    cursor = mydb.cursor()
    cursor.execute("SELECT name, capacity FROM salle;")
    my_table_content = cursor.fetchall()
    print(my_table_content)

    cursor.close()

mydb.close()