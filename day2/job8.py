
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
    
    def is_cage_empty(self, cage_id):
        check_cage = f"SELECT name FROM animal WHERE cage_id = {cage_id};"
        self.cursor.execute(check_cage)
        is_full = self.cursor.fetchone()
        if not is_full:
            return True
        else:
            return False
    
    def check_breed(self, cage_id, breed):
        if self.is_cage_empty(cage_id) == True:
            return True
        else:
            check_breed = f"SELECT breed FROM animal WHERE cage_id = {cage_id};"
            self.cursor.execute(check_breed)
            breeds = self.cursor.fetchall()

            for breed_query in breeds:
                if breed_query[0] == breed:
                    return True
                else:
                    return False
            
    def check_max_capacity(self, cage_id):
        query = f"SELECT COUNT(*) FROM animal WHERE cage_id = {cage_id};"
        self.cursor.execute(query)
        final_number = self.cursor.fetchone()[0]

        check_max_capacity = f"SELECT max_capacity FROM cage WHERE id = {cage_id}"
        self.cursor.execute(check_max_capacity)
        max_capacity = self.cursor.fetchone()[0]

        if final_number == max_capacity:
            return True
        else:
            return False
        
    def does_animal_exist(self, name, breed, birthday):
        query = f"SELECT name FROM animal WHERE name = '{name}' AND breed = '{breed}' AND birthday = {birthday};"
        self.cursor.execute(query)
        does_exist = self.cursor.fetchone()
        if does_exist == None:
            return False
        else:
            return True
        
    def is_cage(self, cage_id):
        query = f"SELECT id FROM cage WHERE id = '{cage_id}';"
        self.cursor.execute(query)
        does_exist = self.cursor.fetchone()
        if does_exist == None:
            return False
        else:
            return True

    def is_empty(self, cage_id):
        query = f"SELECT COUNT(*) FROM animal WHERE cage_id = {cage_id};"
        self.cursor.execute(query)
        does_exist = self.cursor.fetchone()
        if does_exist[0] > 0:
            return False
        else:
            return True

    # Create
    def add_cage(self, area, max_capacity):
        values = (area, max_capacity)
        query = f"INSERT INTO cage (area, max_capacity) VALUES {values};"
        self.cursor.execute(query)
        self.database.commit()

    def add_animal(self, name, breed, cage_id, birth, country):
        if self.does_animal_exist(name, breed, birth):
            print("Vous ne pouvez pas ajouter deux fois le même animal")
        elif not self.check_breed(cage_id, breed):
            print("Vous ne pouvez pas ajouter deux animaux de races différentes dans la même cage.")
        elif self.check_max_capacity(cage_id):
            print("La cage que vous avez choisi a atteint sa capacité maximum, vous ne pouvez pas y ajouter d'animal.")
        else:
            values = (name, breed, cage_id, birth, country)
            query = f"INSERT INTO animal (name, breed, cage_id, birthday, country) VALUES {values};"
            self.cursor.execute(query)
            self.database.commit()

            self.display_an_animal(name, breed, birth)

    # Read   
    def display_all_zoo(self):
        query = f"SELECT * FROM animal;"
        self.cursor.execute(query)
        animals = self.cursor.fetchall()

        print("__ INFORMATIONS DU ZOO __")

        print("\nANIMAUX")
        for animal in animals:
            self.display_an_animal(animal[1],animal[2],animal[4])
        print("\n")

        second_query = f"SELECT * FROM cage;"
        self.cursor.execute(second_query)
        cages = self.cursor.fetchall()

        print("\nCAGES")
        for cage in cages:
            print(f"ID : {cage[0]:03d}  |",
                f"SUPERFICIE : {cage[1]:03d}m² |",
                f"CAPACITE : {cage[2]:03d}", sep="")
        print("\n")

    def get_all_cage_areas(self):
        query = "SELECT SUM(area) FROM cage;"
        self.cursor.execute(query)
        areas = self.cursor.fetchone()[0]
        print(f"La surperficie de toutes les cages est de {areas}m²")

    def display_an_animal(self, name, breed, birth):
        query = f"SELECT * FROM animal WHERE name = '{name}' AND breed = '{breed}' AND birthday = {birth};"
        self.cursor.execute(query)
        animal_info = self.cursor.fetchall()

        for info in animal_info:
            print(f"ID : {info[0]:<3}|",
                f"NOM : {info[1]:<15}|",
                f"RACE : {info[2]:<15}|",
                f"ANNEE : {info[4]:<6}|",
                f"PAYS : {info[5]:<20}|",
                f"CAGE N°{info[3]:<3}", sep="")

    def display_all_animals_in_cage(self, cage_id):
        query = f"SELECT * FROM animal WHERE cage_id = {cage_id};"
        self.cursor.execute(query)
        animals = self.cursor.fetchall()

        for animal in animals:
            print(f"ID : {animal[0]:<3}|",
                f"NOM : {animal[1]:<15}|",
                f"RACE : {animal[2]:<15}|",
                f"ANNEE : {animal[4]:<6}|",
                f"PAYS : {animal[5]:<20}|",
                f"CAGE N°{animal[3]:<3}", sep="")
        print("\n")

    # Update
    def change_cage(self, new_cage_id, name, breed):
        if self.check_breed(new_cage_id, breed):
            query = f"UPDATE animal SET cage_id = {new_cage_id} WHERE name = '{name}' and breed = '{breed}';"
            self.cursor.execute(query)
            self.database.commit()
        else:
            print("La nouvelle cage que vous avez choisi a contient un animal qui ne peut pas s'entendre avec l'animal à déplacer (prédateur - proie).")

    def change_name(self, new_name, name, breed, birth):
        if self.does_animal_exist(name, breed, birth):
            query = f"UPDATE animal SET name = '{new_name}' WHERE name = '{name}' AND breed = '{breed}' AND birthday = {birth};"
            self.cursor.execute(query)
            self.cursor.fetchone()
            self.database.commit()
        else:
            print("Vous ne pouvez pas modifier le nom d'un animal avec le nom d'un animal de la même race déjà existant")

    def change_breed(self, new_breed, name, breed, birth):
        if self.does_animal_exist(name, breed, birth):
            query = f"UPDATE animal SET breed = {new_breed} WHERE name = '{name}' and breed = '{breed}';"
            self.cursor.execute(query)
            self.database.commit()
        else:
            print("Vous ne pouvez pas modifier la race d'un animal avec la race d'un animal du même nom déjà existant")

    def change_birthday(self, new_birthday, name, breed):
        query = f"UPDATE animal SET birthday = {new_birthday} WHERE name = '{name}' and breed = '{breed}';"
        self.cursor.execute(query)
        self.database.commit()
    
    def change_cage_max_capacity(self, new_value, id):
        self.cursor.execute(f"UPDATE cage SET max_capacity = {new_value} WHERE id = '{id}';")
        self.database.commit()

    # Delete
    def move_away_animal(self, name, breed, birth):
        if self.does_animal_exist(name, breed, birth):
            query = f"DELETE FROM animal WHERE name = '{name}' AND breed = '{breed}' AND birthday = {birth};"
            self.cursor.execute(query)
            self.database.commit()
        else:
            print("Vous ne pouvez pas déplacer un animal inexistant.")
    
    def delete_cage(self, cage_id):
        if self.is_cage(cage_id) and self.is_empty(cage_id):
            query = f"DELETE FROM cage WHERE id = '{cage_id}';"
            self.cursor.execute(query)
            self.database.commit()
        else:
            print("Vous ne pouvez pas supprimer une cage inexistante.")

def main():
    my_database = DatabaseZoo()
    my_database.create_database() # add bool if database exist or not, if not create table and else, do not create
    zoo_database = my_database.connect_to_database("zoo_base")
    if zoo_database.is_connected():
        cursor = zoo_database.cursor()
        cage_values = f"(id INT PRIMARY KEY AUTO_INCREMENT NOT NULL, \
                area INT NOT NULL, \
                max_capacity INT)"
        
        my_database.create_tables(cursor, 'cage', f"{cage_values}")

        animal_values = f"(id INT PRIMARY KEY AUTO_INCREMENT NOT NULL, \
                name VARCHAR (255) NOT NULL, \
                breed VARCHAR (255) NOT NULL, \
                cage_id INT NOT NULL, \
                birthday INT NOT NULL, \
                country VARCHAR (255) NOT NULL, \
                FOREIGN KEY (cage_id) REFERENCES cage(id))"
        
        my_database.create_tables(cursor, 'animal', f"{animal_values}")
        my_zoo = ZooData(zoo_database, cursor)

        if not my_database.is_table_full(cursor, 'cage'):
            my_zoo.add_cage(5, 1)
            my_zoo.add_cage(100, 5)
            my_zoo.add_cage(20, 2)
            my_zoo.add_cage(50, 3)
            my_zoo.add_cage(15, 2)
        
        if not my_database.is_table_full(cursor, 'animal'):
            my_zoo.add_animal('Simba', 'Lion', 2, 2016, 'Afrique du Sud')
            my_zoo.add_animal('Luna', 'Panda géant', 3, 2018, 'Chine')
            my_zoo.add_animal('Balthazar', 'Girafe', 4, 2014, 'Kenya')
            my_zoo.add_animal('Maximus', 'Singe', 5, 2015, 'République du Congo')
            my_zoo.add_animal('Pongo', 'Singe', 5, 2013, 'Malaisie')
            my_zoo.add_animal('Toto', 'Crocodile', 1, 2010, 'Égypte')
        
        my_zoo.add_animal('Croco', 'Crocodile', 1, 2003, 'Égypte')

        my_zoo.change_cage(2, 'Luna', 'Panda géant')

        my_zoo.change_name('Louna', 'Luna', 'Panda Géant', 2018)
        my_zoo.display_an_animal('Louna', 'Panda Géant', 2018)

        my_zoo.move_away_animal('Louna', 'Panda Géant', 2018)
        my_zoo.delete_cage(7)
        my_zoo.delete_cage(3)

        my_zoo.add_cage(150, 7)
        
        my_zoo.display_all_zoo()

        my_zoo.get_all_cage_areas()
        cursor.close()
    zoo_database.close()
    
main()