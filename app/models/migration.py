from db_conn import DatabaseConnection
import psycopg2


class Migration(DatabaseConnection):

    def __init__(self):
        super().__init__()

    def drop_tables(self):
        commands = (
        """ 
        DROP TABLE USERS CASCADE
        """,
        """
        DROP TABLE MESSAGES CASCADE
        """,
        """ 
        DROP TABLE GROUPS CASCADE
        """,
        """ 
        DROP TABLE MEMBERS CASCADE
        """
        )
        for command in commands:
            self.cursor.execute(command)
    

    def create_tables(self):
        """ create tables in the PostgreSQL database"""
        commands = (
        """ CREATE TABLE IF NOT EXISTS USERS (
            ID SERIAL PRIMARY KEY UNIQUE,
            FIRSTNAME VARCHAR(50) NOT NULL,
            LASTNAME VARCHAR(50) NOT NULL,
            EMAIL VARCHAR(50) not null UNIQUE,
            PASSWORD VARCHAR(50) NOT NULL,
            PHONE_NUMBER VARCHAR(50),
            ROLE VARCHAR(50) NOT NULL,
            createdOn timestamp(6) without time zone
            )
        """,
        """ CREATE TABLE IF NOT EXISTS MESSAGES (
            MESSAGE_ID  SERIAL PRIMARY KEY UNIQUE,
            USER_ID INTEGER,
            FOREIGN KEY(USER_ID) REFERENCES USERS(ID),
            SUBJECT VARCHAR(50) NOT NULL,
            MESSAGE VARCHAR(1000) NOT NULL,
            PARENTMESSAGEID INTEGER NOT NULL,
            STATUS VARCHAR(25) NOT NULL,
            READ BOOLEAN,
            createdOn timestamp(6) without time zone
            )
        """,
        """ 
            CREATE TABLE IF NOT EXISTS GROUPS (
            ID  SERIAL PRIMARY KEY UNIQUE,
            ADMIN_ID INTEGER,
            FOREIGN KEY(ADMIN_ID) REFERENCES USERS(ID),
            GROUP_NAME VARCHAR(50) NOT NULL,
            createdOn timestamp(6) without time zone
            )
        """, 
        """ 
            CREATE TABLE IF NOT EXISTS MEMBERS (
            GROUP_ID  SERIAL PRIMARY KEY UNIQUE,
            FOREIGN KEY(GROUP_ID) REFERENCES GROUPS(ID),
            MEMBER_ID INTEGER,
            FOREIGN KEY(MEMBER_ID) REFERENCES USERS(ID),
            ROLE VARCHAR(10) NOT NULL,
            createdOn timestamp(6) without time zone
        )
        """,
        """ INSERT INTO USERS(FIRSTNAME, LASTNAME, EMAIL, PASSWORD, ROLE)VALUES('AHMAD','KYAKUS','KYAKUSAHMED@GMAIL.COM','813r312','ADMIN')
        """    
        )
        for command in commands:
            try:
                self.cursor.execute(command)
            except psycopg2.IntegrityError as identifier:
                pass


mig = Migration()
mig.drop_tables()
mig.create_tables()

