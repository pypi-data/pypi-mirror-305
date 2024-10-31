import sqlite3
import pandas as pd

class SQLiteConnector:
    def __init__(self, db_path):
        self.conn = sqlite3.connect(db_path)

    def execute_query(self, query):
        return pd.read_sql(query, self.conn)

    def close_connection(self):
        self.conn.close()