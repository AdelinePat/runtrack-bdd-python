import mysql.connector

mydatabase = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="LaPlateforme"
)

if mydatabase.is_connected():
    cursor = mydatabase.cursor()
    cursor.execute("SELECT capacity FROM salle")
    capacities = cursor.fetchall()

    total_capacity = 0
    for capacity in capacities:
        total_capacity += capacity[0]
    cursor.close()

mydatabase.close()

print(f"La capacité  de toutes les salles est de : {total_capacity}")