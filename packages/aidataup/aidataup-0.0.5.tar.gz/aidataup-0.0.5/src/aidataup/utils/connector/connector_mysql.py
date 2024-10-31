import mysql.connector
import pandas as pd

class MySQLConnector:
    def __init__(self, host, database, user, password):
        self.conn = mysql.connector.connect(
            host=host, database=database, user=user, password=password
        )

    def execute_query(self, query):
        return pd.read_sql(query, self.conn)

    def close_connection(self):
        self.conn.close()