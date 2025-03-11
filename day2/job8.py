
import mysql.connector

class DatabaseZoo():
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

            if "zoo_base" not in all_data_bases:
                cursor.execute("CREATE DATABASE zoo_base;")
                cursor.execute("USE zoo_base;")

            cursor.close()
        my_server.close()

    def create_tables(self, cursor, table_name, values):
        cursor.execute("SHOW TABLES;")
        tables = cursor.fetchall()

        all_tables = []
        for table in tables:
            all_tables.append(table[0])

        if table_name not in all_tables:
            query = f"CREATE TABLE {table_name} {values}"
            cursor.execute(query)

    def is_table_full(self, cursor, table_name):
        cursor.execute(f"TABLE {table_name};")
        is_empty = cursor.fetchall()
        if is_empty == []:
            return False
        else:
            return True

class ZooData():
    def __init__(self, database, cursor):
        self.cursor = cursor
        self.database = database

    # Create
    def add_cage(self, area, max_capacity):
        values = (area, max_capacity)
        query = f"INSERT INTO cage (area, max_capacity) VALUES {values};"
        self.cursor.execute(query)
        self.database.commit()

    def add_animal(self, name, breed, cage_id, birth, country):
        check_query = f"SELECT name FROM animal WHERE name = '{name}' AND breed = '{breed}';"
        self.cursor.execute(check_query)
        if bool(self.cursor.fetchall()):
            print("Vous ne pouvez pas ajouter deux fois le même animal")
        else:
            values = (name, breed, cage_id, birth, country)
            query = f"INSERT INTO animal (name, breed, cage_id, birthday, country) VALUES {values};"
            self.cursor.execute(query)
            self.database.commit()

#     # Read
#     def display_employee(self, lastname, firstname):
#         print(f"\n ### Information de l'employé {lastname} ###")
#         self.cursor.execute(f"SELECT * FROM employee WHERE lastname = '{lastname}' AND firstname = '{firstname}';")
#         return self.cursor.fetchall()
    
#     def display_all_employee(self):
#         print(f"\n ### Liste de tous les employés ###")
#         self.cursor.execute(f"TABLE employee")
#         employees = self.cursor.fetchall()

#         for employee in employees:
#             self.cursor.execute(f"SELECT service_name FROM service WHERE id = {employee[4]}")
#             service_name = self.cursor.fetchone()
#             print(f"{employee[0]} | {employee[1]} {employee[2]} | {employee[3]}€ | {service_name[0]}")

#     def display_from_salary(self, salary):
#         print(f"\n ### Liste des employés ayant un salaire supérieur à {salary}€ ###")
#         self.cursor.execute(f"SELECT * FROM employee WHERE salary > {salary};")
#         people = self.cursor.fetchall()

#         for person in people:
#             self.cursor.execute(f"SELECT service_name FROM service WHERE id = {person[4]}")
#             service_name = self.cursor.fetchone()zoo_base
#             print(f"Nom : {person[1]} | Prénom : {person[2]} | Salaire : {person[3]}€ | Service : {service_name[0]}")
    
#     def display_services(self):
#         print(f"\n ### Liste des services de l'entreprise ###")
#         self.cursor.execute("TABLE service")
#         services = self.cursor.fetchall()

#         for service in services:
#             print(f"ID : {service[0]} | NOM : {service[1]}")

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

def main():
    my_database = DatabaseZoo()
    my_database.create_database() # add bool if database exist or not, if not create table and else, do not create table
    zoo_database = my_database.connect_to_database("zoo_base")
    if zoo_database.is_connected():
        cursor = zoo_database.cursor()
        # table_name, values
        cage_values = f"(id INT PRIMARY KEY AUTO_INCREMENT NOT NULL, \
                area INT NOT NULL, \
                max_capacity INT)"
        
        my_database.create_tables(cursor, 'cage', f"{cage_values}")

        animal_values = f"(id INT PRIMARY KEY AUTO_INCREMENT NOT NULL, \
                name VARCHAR (255) NOT NULL, \
                breed VARCHAR (255) NOT NULL, \
                cage_id INT NOT NULL, \
                birthday INT NOT NULL, \
                country VARCHAR (255) NOT NULL)"
        
        my_database.create_tables(cursor, 'animal', f"{animal_values}")
        my_zoo = ZooData(zoo_database, cursor)

        if not my_database.is_table_full(cursor, 'cage'):
            my_zoo.add_cage(5, 1)
            my_zoo.add_cage(100, 5)
            my_zoo.add_cage(20, 2)
            my_zoo.add_cage(50, 3)
            my_zoo.add_cage(15, 2)
        
        if not my_database.is_table_full(cursor, 'animal'):
            # name, breed, cage_id, birth, country
            my_zoo.add_animal('Simba', 'Lion', 2, 2016, 'Afrique du Sud')
            my_zoo.add_animal('Luna', 'Panda géant', 3, 2018, 'Chine')
            my_zoo.add_animal('Balthazar', 'Girafe', 4, 2014, 'Kenya')
            my_zoo.add_animal('Maximus', 'Gorille', 5, 2015, 'République du Congo')
            my_zoo.add_animal('Pongo', 'Orang-outan', 5, 2013, 'Malaisie')
            my_zoo.add_animal('Toto', 'Crocodile', 1, 2010, 'Égypte')
       
        # my_employees.display_from_salary(3000)
        
        # my_employees.display_from_salary(2000)

        # my_employees.update_info("id_service", 5, "Lambert", "Claire")

        # my_employees.display_services()
        # my_employees.display_all_employee()

        # print(my_employees.display_employee('Martin', 'Lucas'))

        # my_employees.delete_employee('Bernard', 'Sophie')
        # my_employees.add_employee('Bahl', 'Safia', 1400.75, 3)

        # print(my_employees.display_all_employee())

        cursor.close()DATABASE