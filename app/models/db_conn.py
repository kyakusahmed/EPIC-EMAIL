import psycopg2
from datetime import datetime


class DatabaseConnection:

    def __init__(self):
        try:

            self.conn = psycopg2.connect(
            database="d7v2uinklja1tk",
            user="fswwqztrgjtaxx",
            password="7198b7980e271aa8798a4fe65407746e0e7cc34c6e99a3afd3184cd1d928d4f7",
            port="5432",
            host="ec2-107-20-177-161.compute-1.amazonaws.com"
            )
            self.conn.autocommit = True
            self.cursor = self.conn.cursor()
            print("connected")


        #     self.conn = psycopg2.connect(
        #         database="epic", user="postgres", password=1988, port="5432",
        #         host="127.0.0.1"
        #     )
        #     self.conn.autocommit = True
        #     self.cursor = self.conn.cursor()
        # except Exception as ex:
        #     print("connection failed {}".format(ex))
