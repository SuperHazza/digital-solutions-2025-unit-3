import sqlite3
import csv


class Datastore:
    """
    Datastore for the netflix database
    """

    def __init__(self, database_file: str, data_file: str):
        """
        initialises the datastore
        """
        self.database_file = database_file
        self.data_file = data_file
        self.conn = sqlite3.connect(self.database_file)
        self.cursor = self.conn.cursor()

        self.populate_database()

    def populate_database(self):
        """
        populates the database with data from the csv file
        """
        with open(self.data_file, mode="r", encoding="utf-8") as csvfile:
            csv_reader = csv.DictReader(csvfile)

            # process the CSV data
            for record in csv_reader:
                print(record)