from aidataup.utils.connector.connector_postgresql import PostgresConnector
from aidataup.utils.connector.connector_mysql import MySQLConnector
from aidataup.utils.connector.connector_sqlite import SQLiteConnector

class DatabaseManager:
    def __init__(self, db_type, **kwargs):

        if db_type == 'postgres':
            self.connector = PostgresConnector(**kwargs)
        elif db_type == 'mysql':
            self.connector = MySQLConnector(**kwargs)
        elif db_type == 'sqlite':
            self.connector = SQLiteConnector(**kwargs)
        else:
            raise ValueError(f"Not support : {db_type}")

    def execute_query(self, query):
        return self.connector.execute_query(query)

    def close(self):
        self.connector.close_connection()




# from aidataup.utils.database_manager import DatabaseManager
# # ==== postgres use example
# postgres_db = DatabaseManager(db_type='postgres',host='localhost',database='mydb',user='user',password='password')
# df = postgres_db.execute_query('SELECT * FROM my_table')
# print(df.head()) #----> Display data frame
# postgres_db.close() #----> Close connection

# # ==== sqlite use example
# sqlite_db = DatabaseManager(db_type='sqlite', db_path='my_database.db')
# df = sqlite_db.execute_query('SELECT * FROM another_table')
# print(df.head()) #----> Display data frame
# sqlite_db.close() #----> Close connection