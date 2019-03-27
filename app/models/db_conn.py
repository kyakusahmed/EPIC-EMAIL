import psycopg2
from datetime import datetime


class DatabaseConnection:

    def __init__(self):
        try:

            self.conn = psycopg2.connect(
                database="epic", user="postgres", password=1988, port="5432",
                host="127.0.0.1"
            )
            self.conn.autocommit = True
            self.cursor = self.conn.cursor()
            print('connected')
            print('connected')
        except Exception as ex:
            print("connection failed {}".format(ex))
