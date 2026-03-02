import sqlite3


class DBProxy:
    def __init__(self, db_name: str):
        # Establish a connection to the SQLite database file
        self.db_name = db_name
        self.connection = sqlite3.connect(db_name)

        # Ensure the 'dados' table exists; create it if it doesn't.
        # Uses 'id' as an auto-incrementing primary key for unique record tracking.
        self.connection.execute('''
                                   CREATE TABLE IF NOT EXISTS dados(
                                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                                   name TEXT NOT NULL,
                                   score INTEGER NOT NULL,
                                   date TEXT NOT NULL)
                                '''
                                )

    def save(self, score_dict: dict):
        # Using named placeholders (:name, etc.) is a security best practice
        # to prevent SQL Injection attacks.
        self.connection.execute('INSERT INTO dados (name, score, date) VALUES (:name, :score, :date)', score_dict)
        # Commit ensures the transaction is actually written to the disk.
        self.connection.commit()

    def retrieve_top10(self) -> list:
        # ORDER BY score DESC ensures the highest numbers appear first.
        return self.connection.execute('SELECT * FROM dados ORDER BY score DESC LIMIT 10').fetchall()

    def close(self):
        return self.connection.close()
