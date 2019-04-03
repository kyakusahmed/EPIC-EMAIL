from app.models.db_conn import DatabaseConnection
from datetime import datetime
import psycopg2


class User(DatabaseConnection):

    def __init__(self):
        super().__init__()

    def create_user_account(self, firstname, lastname, email, password):
        command = """
        INSERT INTO USERS (
            firstname, lastname, email, password, role, createdon) VALUES(
                '{}','{}','{}','{}','{}','{}')
        """.format(
            firstname, lastname, email, password, "user", datetime.now())
        self.cursor.execute(command)
        return "user registered successfully"

    def user_signin(self, email, password):
        try:
            command = """
            SELECT * FROM USERS WHERE EMAIL= '{}' AND PASSWORD = '{}'
            """.format(email, password)
            self.cursor.execute(command)
            user1 = self.cursor.fetchone()
            return user1
        except Exception as ex:
            return "failed {}".format(ex)

    def get_user_by_email(self, email):
        command = """
        SELECT * FROM USERS WHERE EMAIL='{}'
        """.format(email)
        self.cursor.execute(command)
        user = self.cursor.fetchone()
        return user

    def search_user_by_email(self, email):
        command = """
        SELECT * FROM USERS WHERE email ='{}'
        """.format(email)
        self.cursor.execute(command)
        user = self.cursor.fetchone()
        return user

    def search_user_by_id(self, id):
        command = """
        SELECT * FROM USERS WHERE id ='{}'
        """.format(id)
        self.cursor.execute(command)
        user = self.cursor.fetchone()
        return user

    def get_all_users(self):
        command = """
        SELECT * FROM USERS 
        """.format()
        self.cursor.execute(command)
        data = self.cursor.fetchall()
        return data


    
