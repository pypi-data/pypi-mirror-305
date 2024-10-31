import pandas as pd
import psycopg2

def connect_to_postgres(host, database, user, password):
    conn = psycopg2.connect(
        host=host,
        database=database,
        user=user,
        password=password
    )
    return conn

def read_sql_to_dataframe(query, conn):
    
    df = pd.read_sql(query, conn)
    return df



class PostgresConnector:
    def __init__(self, host, database, user, password):
        self.conn = psycopg2.connect(
            host=host, database=database, user=user, password=password
        )

    def execute_query(self, query):
        return pd.read_sql(query, self.conn)

    def close_connection(self):
        self.conn.close()

