from csv import DictReader
from os.path import join
from sqlite3 import connect, Row
from typing import Type

from ..models import Accessoires, Fiets, Medewerker, Klant


class DatabaseConnection:
    def __init__(self):
        self._connection = connect('Accessoires.db')
        self._connection.row_factory = Row
        self._connection = connect('Fiets.db')
        self._connection.row_factory = Row
        self._connection = connect('Medewerker.db')
        self._connection.row_factory = Row
        self._connection = connect('Klant.db')
        self._connection.row_factory = Row

        self.createDB()

    def createDB(self):
        # Create Accessoires table
        self.connection.execute("DROP TABLE IF EXISTS Accessoires")
        self.connection.execute("DROP TABLE IF EXISTS Fiets")
        self.connection.execute("DROP TABLE IF EXISTS Medewerker")
        self.connection.execute("DROP TABLE IF EXISTS Klant")
        self.connection.commit()

        self.connection.execute("""CREATE TABLE IF NOT EXISTS Accessoires (
                    merk VARCHAR(255) NOT NULL,
                    types VARCHAR(255) NOT NULL,
                    dagprijs INTEGER NOT NULL,
                    nieuwprijs INTEGER NOT NULL
                );""")
        self.connection.execute("""CREATE TABLE IF NOT EXISTS Fiets (
                    types VARCHAR(255) NOT NULL,
                    merk VARCHAR(255) NOT NULL,
                    dagprijs INTEGER NOT NULL,
                    borg INTEGER NOT NULL
                );""")

        self.connection.execute("""CREATE TABLE IF NOT EXISTS Medewerker (
                    voornaam VARCHAR(255) NOT NULL,
                    achternaam VARCHAR(255) NOT NULL,
                    rol VARCHAR(255) NOT NULL,
                    loginnaam VARCHAR(255) NOT NULL
                );""")
        self.connection.execute("""CREATE TABLE IF NOT EXISTS Klant (
                    achternaam text (25) NOT NULL, 
                    voornaam text (15) NOT NULL,
                    adres varchar (27) NOT NULL,
                    postcode varchar (10) NOT NULL,
                    woonplaats text (19) NOT NULL,
                    land text (19) NOT NULL
                );""")
        self.connection.commit()
        print('Table is created successfully')

        self.read_csv_insert_db(join('assets', 'data', 'accessories.csv'), Accessoires, 'Accessoires')
        self.read_csv_insert_db(join('assets', 'data', 'fietsen.csv'), Fiets, 'Fiets')
        self.read_csv_insert_db(join('assets', 'data', 'klant.csv'), Klant, 'Klant')
        self.read_csv_insert_db(join('assets', 'data', 'medewerker.csv'), Medewerker, 'Medewerker')

    def read_csv_insert_db(self, file, object_type: Type, table):
        """
        Read a csv file, and put the objects in the database.
        """
        with open(file, 'r') as data:
            reader = DictReader(data)

            # For every row in the csv file, create an instance of the provided object type
            # and insert it into a table in the database that matches the provided table name
            for row in reader:
                instance = object_type(row)

                # Get the amount of values to insert into the table
                attribute_count = '?, ' * len(instance.attributes())
                attribute_count = attribute_count[0: len(attribute_count) - 2]

                self.connection.execute(
                    f'INSERT INTO {table} {instance.attributes()} VALUES ({attribute_count});', tuple(instance.values())
                )

        self.connection.commit()

    def get_data(self, table: str, object_type: Type):
        cursor = self._connection.cursor()
        cursor.execute(f'SELECT * FROM {table}')

        rows = cursor.fetchall()

        objects = []

        for row in rows:
            objects.append(object_type(dict(row)))

        return objects

    @property
    def connection(self):
        return self._connection
