import mysql.connector

class Employees():
    def __init__(self, employee_database, cursor):
        self.cursor = cursor
        self.employee_database = employee_database

    # Create
    def add_service(self, service_name):
        self.cursor.execute(f"INSERT INTO service (service_name) VALUES ('{service_name}');")
        self.employee_database.commit()

    def add_employee(self, lastname, firstname, salary, id_service):
        self.cursor.execute(f"SELECT lastname FROM employee WHERE lastname = '{lastname}' AND firstname = '{firstname}' AND salary = {salary} AND id_service = {id_service};")
        employee = self.cursor.fetchall()

        if bool(employee):
            print("Vous ne pouvez pas créer 2 employés identitques")
        else:
            self.cursor.execute(f"INSERT INTO employee (lastname, firstname, salary, id_service) VALUES ('{lastname}', '{firstname}', {salary}, {id_service});")
            self.employee_database.commit()
    # Read
    def display_employee(self, lastname, firstname):
        print(f"\n ### Information de l'employé {lastname} ###")
        self.cursor.execute(f"SELECT * FROM employee WHERE lastname = '{lastname}' AND firstname = '{firstname}';")
        return self.cursor.fetchall()
    
    def display_all_employee(self):
        print(f"\n ### Liste de tous les employés ###")
        self.cursor.execute(f"TABLE employee")
        employees = self.cursor.fetchall()

        for employee in employees:
            self.cursor.execute(f"SELECT service_name FROM service WHERE id = {employee[4]}")
            service_name = self.cursor.fetchone()
            print(f"{employee[0]} | {employee[1]} {employee[2]} | {employee[3]}€ | {service_name[0]}")

    def display_from_salary(self, salary):
        print(f"\n ### Liste des employés ayant un salaire supérieur à {salary}€ ###")
        self.cursor.execute(f"SELECT * FROM employee WHERE salary > {salary};")
        people = self.cursor.fetchall()

        for person in people:
            self.cursor.execute(f"SELECT service_name FROM service WHERE id = {person[4]}")
            service_name = self.cursor.fetchone()
            print(f"Nom : {person[1]} | Prénom : {person[2]} | Salaire : {person[3]}€ | Service : {service_name[0]}")
    
    def display_services(self):
        print(f"\n ### Liste des services de l'entreprise ###")
        self.cursor.execute("TABLE service")
        services = self.cursor.fetchall()

        for service in services:
            print(f"ID : {service[0]} | NOM : {service[1]}")

    # Update
    def update_info(self, info_to_change, new_value, lastname, firstname):
        if info_to_change == "salary":
            self.cursor.execute(f"UPDATE employee SET salary = {new_value} WHERE lastname = '{lastname}' and firstname = '{firstname}';")
        elif info_to_change == "id_service":
            self.cursor.execute(f"UPDATE employee SET id_service = {new_value} WHERE lastname = '{lastname}' and firstname = '{firstname}';")
        elif info_to_change == "lastname":
            self.cursor.execute(f"UPDATE employee SET lastname = '{new_value}' WHERE lastname = '{lastname}' and firstname = '{firstname}';")
        elif info_to_change == "firstname":
            self.cursor.execute(f"UPDATE employee SET firstname = '{new_value}' WHERE lastname = '{lastname}' and firstname = '{firstname}';")
        self.employee_database.commit()

    # Delete
    def delete_employee(self, lastname, firstname):
        self.cursor.execute(f"SELECT * FROM employee WHERE lastname = '{lastname}' and firstname = '{firstname}';")
        employee = self.cursor.fetchall()
        if not bool(employee):
            print("Vous ne pouvez pas supprimer un(e) employé(e) inexistant(e).")
        else:
            info = self.display_employee(lastname, firstname)
            self.cursor.execute(f"DELETE FROM employee WHERE lastname = '{lastname}' AND firstname = '{firstname}';")
            self.employee_database.commit()
            print(f"{info}\
                \nl'employé(e) {lastname} {firstname} a bien été supprimé(e) de la base de données")

class DatabaseEmployee():
    def connect_to_database(self, database_name):
        database_connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database = database_name
        )
        return database_connection
        

    def create_database(self):
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

            cursor.close()
        my_server.close()

    def create_tables(self, cursor):
        cursor.execute("USE employees_base;")
        cursor.execute("SHOW TABLES;")
        tables = cursor.fetchall()

        all_tables = []
        for table in tables:
            all_tables.append(table[0])

        if "employee" not in all_tables:
            cursor.execute("CREATE TABLE employee (id INT PRIMARY KEY AUTO_INCREMENT NOT NULL, lastname VARCHAR (255) NOT NULL, firstname VARCHAR(255) NOT NULL, salary FLOAT NOT NULL, id_service INT);")
        if "service" not in all_tables:
            cursor.execute("CREATE TABLE service (id INT PRIMARY KEY AUTO_INCREMENT NOT NULL, service_name VARCHAR (255) NOT NULL);")

    def is_table_full(self, cursor, table_name):
        match table_name:
            case "service":
                cursor.execute("TABLE service;")
            case "employee":
                cursor.execute("TABLE employee;")

        is_empty = cursor.fetchall()
        if is_empty == []:
            return False
        else:
            return True
        # return bool(is_empty)

def main():
    my_database = DatabaseEmployee()
    my_database.create_database()
    employee_database = my_database.connect_to_database("employees_base")
    if employee_database.is_connected():
        cursor = employee_database.cursor()
        my_database.create_tables(cursor)
        my_employees = Employees(employee_database, cursor)

        if not my_database.is_table_full(cursor, 'service'):
            my_employees.add_service('Logistique')
            my_employees.add_service('Ressource Humaine')
            my_employees.add_service('Informatique')
            my_employees.add_service('Marketing')
            my_employees.add_service('Finance')
        
        if not my_database.is_table_full(cursor, 'employee'):
            my_employees.add_employee('Dupont', 'Marie', 3200.0, 1)
            my_employees.add_employee('Lefevre', 'Julien', 2800.50, 2)
            my_employees.add_employee('Bernard', 'Sophie', 3500.75, 3)
            my_employees.add_employee('Moreau', 'Thomas', 4100.80, 4)
            my_employees.add_employee('Lambert', 'Claire', 2600, 0)
            my_employees.add_employee('Martin', 'Lucas', 2900.5, 1)
       
        my_employees.display_from_salary(3000)
        
        my_employees.display_from_salary(2000)

        my_employees.update_info("id_service", 5, "Lambert", "Claire")

        my_employees.display_services()
        my_employees.display_all_employee()

        print(my_employees.display_employee('Martin', 'Lucas'))

        my_employees.delete_employee('Bernard', 'Sophie')
        my_employees.add_employee('Bahl', 'Safia', 1400.75, 3)

        print(my_employees.display_all_employee())

        cursor.close()

    employee_database.close()

main()
