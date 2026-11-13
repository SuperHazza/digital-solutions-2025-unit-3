import ast
import csv
import sqlite3


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
        self.conn.commit()

    def populate_database(self):
        """
        populates the database with data from the csv file
        """
        with open(self.data_file, mode="r", encoding="utf-8") as csvfile:
            csv_reader = csv.DictReader(csvfile)

            # process the CSV data
            for record in csv_reader:
                # process types values
                type_name = record["type"]

                # view the type data
                type_id = self.add_type(
                    type_name,
                )

                # processes the rating data
                if record["rating"]:
                    rating_name = record["rating"]

                rating_id = self.add_rating(
                    rating_name,
                )

    def add_type(
        self,
        name: str,
    ):
        """
        adds a type to the database
        """
        self.cursor.execute(
            """
            INSERT OR IGNORE INTO Types (name)
            VALUES (:name)
            """,
            {
                "name": name,
            },
        )

        return self.cursor.lastrowid

    def add_rating(
            self,
            name: str,
        ):
            """
            adds a rating to the database
            """
            self.cursor.execute(
                """
                INSERT OR IGNORE INTO Rating (name)
                VALUES (:name)
                """,
                {
                    "name": name,
                },
            )
    
            return self.cursor.lastrowid
