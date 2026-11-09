import sqlite3


class Datastore:
    """
    Datastore for the f1 driver database
    """

    def __init__(self):
        """
        initialises the datastore
        """

        self.conn = sqlite3.connect("f1_driver.db")
        self.cursor = self.conn.cursor()

        self.build_database()
        self.conn.commit()

    def build_database(self):
        """
        builds the database
        """

        self.cursor.execute(
            """
            CREATE TABLE "Driver" (
                "driver_id"	INTEGER,
                "name"	TEXT NOT NULL,
                "nationality"	TEXT NOT NULL,
                "race_entries"	INTEGER NOT NULL CHECK(race_entries > 0),
                "race_starts"	INTEGER NOT NULL CHECK(race_starts >= 0),
                "pole_positions"	INTEGER NOT NULL CHECK(pole_positions >= 0),
                "race_wins"	INTEGER NOT NULL CHECK(race_wins >= 0),
                "podiums"	INTEGER NOT NULL CHECK(podiums >= 0),
                "fastest_laps"	INTEGER NOT NULL CHECK(fastest_laps >= 0),
                "points"	REAL NOT NULL CHECK(points >= 0),
                PRIMARY KEY("driver_id" AUTOINCREMENT)
            );
            """
        )

        self.cursor.execute(
            """
            CREATE TABLE "Seasons" (
                "year"	INTEGER,
                "champion"	INTEGER NOT NULL,
                PRIMARY KEY("year"),
                FOREIGN KEY("champion") REFERENCES "Driver"("driver_id")
            );
            """
        )

        self.cursor.execute(
            """
            CREATE TABLE "Raced" (
                "driver_id"	INTEGER,
                "year"	INTEGER,
                PRIMARY KEY("driver_id","year"),
                FOREIGN KEY("driver_id") REFERENCES "Driver"("driver_id"),
                FOREIGN KEY("year") REFERENCES "Seasons"("year")
            );
            """
        )
        
db = Datastore()