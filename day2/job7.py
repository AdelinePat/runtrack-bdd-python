import mysql.connector

my_server = mysql.connector.connect(
    host="localhost",
    user="root",
    password=""
)

if my_server.is_connected():
    cursor = my_server.cursor()
    cursor.execute("SHOW DATABASES;")
    databases = cursor.fetchall()

    all_data_bases = []
    for database in databases:
        all_data_bases.append(database[0])

    if "employees_base" not in all_data_bases:
        cursor.execute("CREATE DATABASE employees_base;")

    else:
        cursor.execute("USE employees_base;")
        cursor.execute("SHOW TABLES;")
        tables = cursor.fetchall()

        all_tables = []
        for table in tables:
            all_tables.append(table[0])
        if "employee" not in all_tables:
            cursor.execute("USE employees_base; CREATE TABLE employee (id INT PRIMARY KEY AUTO_INCREMENT NOT NULL, lastname VARCHAR (255) NOT NULL, firstname VARCHAR(255) NOT NULL, salary FLOAT NOT NULL, id_service INT);")
        if "service" not in all_tables:
            cursor.execute("USE employees_base; CREATE TABLE service (id INT PRIMARY KEY AUTO_INCREMENT NOT NULL, service_name VARCHAR (255) NOT NULL);")
    cursor.close()
my_server.close()

employee_database = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database = "employees_base"
)

if employee_database.is_connected():
    cursor = employee_database.cursor()
    cursor.execute("TABLE service;")
    is_service = cursor.fetchall()

    if not is_service:
        cursor.execute("INSERT INTO service (service_name) VALUES ('Logistique'),('Ressource Humaine'), ('Informatique'), ('Marketing'), ('Finance');")

    cursor.execute("TABLE employee")
    is_employee = cursor.fetchall()
    if not is_employee:
        cursor.execute("INSERT INTO employee (lastname, firstname, salary, id_service) VALUES ('Dupont', 'Marie', 3200.0, 1), ('Lefevre', 'Julien', 2800.50, 2), ('Bernard', 'Sophie', 3500.75, 3), ('Moreau', 'Thomas', 4100.80, 4), ('Lambert', 'Claire', 2600, 0);")

    cursor.execute("SELECT * FROM employee WHERE salary > 3000;")
    hight_salary = cursor.fetchall()
    print(hight_salary)

    cursor.close()

employee_database.close()