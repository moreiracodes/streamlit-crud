import pyodbc
import os


class Database:
    def __init__(self):
        string_connection = (
            f"DRIVER={{ODBC Driver 17 for SQL Server}};"
            f'SERVER={os.getenv("DB_SERVER")};'
            f'DATABASE={os.getenv("DB_NAME")};'
            f'UID={os.getenv("DB_USERNAME")};'
            f'PWD={os.getenv("DB_PASSWORD")};'
        )

        try:
            connection = pyodbc.connect(string_connection)
            return connection

        except Exception as e:
            print(f"Connection error: {e}")
