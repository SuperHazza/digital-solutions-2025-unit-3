import csv
import sqlite3
import ast


class Datastore:
    """
    Datastore for the f1 driver database
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
                  # process driver values
                name = record["Driver"]
                nationality = record["Nationality"]
                race_entries = int(float(record["Race_Entries"]))
                race_starts = int(float(record["Race_Starts"]))
                pole_positions = int(float(record["Pole_Positions"]))
                race_wins = int(float(record["Race_Wins"]))
                podiums = int(float(record["Podiums"]))
                fastest_laps = int(float(record["Fastest_Laps"]))
                points = float(record["Points"])

                # view the driver data
                driver_id = self.add_driver(
                    name,
                    nationality,
                    race_entries,
                    race_starts,
                    pole_positions,
                    race_wins,
                    podiums,
                    fastest_laps,
                    points,
                )

                # process only the championship years
                if record["Championship Years"]:
                    years = ast.literal_eval(record["Championship Years"])

                    for year in years:
                        self.add_season(year, driver_id)

                # process driver seasons
                seasons = ast.literal_eval(record["Seasons"])
                for season in seasons:
                    self.add_raced(driver_id, season)

    def add_driver(
        self,
        name: str,
        nationality: str,
        race_entries: int,
        race_starts: int,
        pole_positions: int,
        race_wins: int,
        podiums: int,
        fastest_laps: int,
        points: float,
    ):
        """
        adds a driver to the database
        """
        self.cursor.execute(
            """
            INSERT INTO Driver (name, nationality, race_entries, race_starts, pole_positions, race_wins, podiums, fastest_laps, points)
            VALUES (:name, :nationality, :race_entries, :race_starts, :pole_positions, :race_wins, :podiums, :fastest_laps, :points)
            """,
            {
                "name": name,
                "nationality": nationality,
                "race_entries": race_entries,
                "race_starts": race_starts,
                "pole_positions": pole_positions,
                "race_wins": race_wins,
                "podiums": podiums,
                "fastest_laps": fastest_laps,
                "points": points,
            },
        )                                                   #The : in the SQL statement increase security by preventing SQL injection attacks.


        return self.cursor.lastrowid
    def add_season(self, year: int, champion: int):
        """
        adds a season to the database
        """
        self.cursor.execute(
            """
            INSERT INTO Seasons
            VALUES (:year, :champion)
            """,
            {
                "year": year, 
                "champion": champion
            },
        )

    def add_raced(self, driver_id: int, year: int):
        self.cursor.execute(
            """
            INSERT INTO Raced
            VALUES (:driver_id, :year)
            """,
            {
                "driver_id": driver_id, 
                "year": year
            },
        )