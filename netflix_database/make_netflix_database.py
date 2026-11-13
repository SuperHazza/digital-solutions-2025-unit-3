import sqlite3


class Datastore:
    """
    Datastore for the netflix database
    """

    def __init__(self):
        """
        initialises the datastore
        """

        self.conn = sqlite3.connect("netflix.db")
        self.cursor = self.conn.cursor()

        self.build_database()
        self.conn.commit()

    def build_database(self):
        """
        builds the database
        """

        self.cursor.execute(
            """
            CREATE TABLE "Types" (
	            "Type_ID"	INTEGER,
	            "Name"	TEXT NOT NULL UNIQUE,
	            PRIMARY KEY("Type_ID" AUTOINCREMENT)
            );
            """
        )

        self.cursor.execute(
            """
            CREATE TABLE "Rating" (
                "Rating_ID"	INTEGER,
                "Name"	TEXT NOT NULL UNIQUE,
                PRIMARY KEY("Rating_ID" AUTOINCREMENT)
            );
            """
        )

        self.cursor.execute(
            """
            CREATE TABLE "Show" (
                "Show_ID"	INTEGER,
                "Type"	INTEGER,
                "Title"	TEXT NOT NULL,
                "Date_Added"	TEXT NOT NULL,
                "Release_Year"	INTEGER NOT NULL,
                "Rating"	INTEGER,
                "Duration"	TEXT NOT NULL,
                "Description"	TEXT NOT NULL,
                PRIMARY KEY("Show_ID" AUTOINCREMENT),
                FOREIGN KEY("Rating") REFERENCES "Rating"("Rating_ID"),
                FOREIGN KEY("Type") REFERENCES "Types"("Type_ID")
            );
            """
        )

        self.cursor.execute(
            """
            CREATE TABLE "Director" (
                "Director_ID"	INTEGER,
                "Name"	TEXT NOT NULL,
                PRIMARY KEY("Director_ID" AUTOINCREMENT)
            );
            """
        )

        self.cursor.execute(
            """
            CREATE TABLE "Show_Director" (
                "Show_ID"	INTEGER,
                "Director_ID"	INTEGER,
                PRIMARY KEY("Show_ID","Director_ID"),
                FOREIGN KEY("Director_ID") REFERENCES "Director"("Director_ID"),
                FOREIGN KEY("Show_ID") REFERENCES "Show"("Show_ID")
            );
            """
        )

        self.cursor.execute(
            """
            CREATE TABLE "Country" (
                "Country_ID"	INTEGER,
                "Name"	TEXT NOT NULL,
                PRIMARY KEY("Country_ID" AUTOINCREMENT)
            );
            """
        )

        self.cursor.execute(
            """
            CREATE TABLE "Show_Country" (
                "Show_ID"	INTEGER,
                "Country_ID"	INTEGER,
                PRIMARY KEY("Show_ID","Country_ID"),
                FOREIGN KEY("Country_ID") REFERENCES "Country"("Country_ID"),
                FOREIGN KEY("Show_ID") REFERENCES "Show"("Show_ID")
            );
            """
        )

        self.cursor.execute(
            """
            CREATE TABLE "Actor" (
                "Actor_ID"	INTEGER,
                "Name"	TEXT NOT NULL,
                PRIMARY KEY("Actor_ID" AUTOINCREMENT)
            );
            """
        )

        self.cursor.execute(
            """
            CREATE TABLE "Cast" (
                "Show_ID"	INTEGER,
                "Actor_ID"	INTEGER,
                PRIMARY KEY("Show_ID","Actor_ID"),
                FOREIGN KEY("Actor_ID") REFERENCES "Actor"("Actor_ID"),
                FOREIGN KEY("Show_ID") REFERENCES "Show"("Show_ID")
            );
            """
        )

        self.cursor.execute(
            """
            CREATE TABLE "Category" (
                "Category_ID"	INTEGER,
                "Name"	TEXT NOT NULL,
                PRIMARY KEY("Category_ID" AUTOINCREMENT)
            );
            """
        )

        self.cursor.execute(
            """
            CREATE TABLE "Show_Category" (
                "Show_ID"	INTEGER,
                "Category_ID"	INTEGER,
                PRIMARY KEY("Show_ID","Category_ID"),
                FOREIGN KEY("Category_ID") REFERENCES "Category"("Category_ID"),
                FOREIGN KEY("Show_ID") REFERENCES "Show"("Show_ID")
            );
            """
        )


db = Datastore()