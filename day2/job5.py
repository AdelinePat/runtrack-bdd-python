import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password= "",
    database="LaPlateforme"
)

if mydb.is_connected():
  
    cursor = mydb.cursor()
    cursor.execute("SELECT SUM(area) FROM etage;")
    surface_area = cursor.fetchone()[0]
    # print(areas)

    # surface_area = 0
    # for area in areas:
    #     print(area[0])
    #     surface_area += area[0]
    cursor.close()

mydb.close()

print(f"La superficie de La Plateforme est de {surface_area}m²")