from app.models.db_conn import DatabaseConnection
from datetime import datetime
import psycopg2


class Group(DatabaseConnection):

    def __init__(self):
        super().__init__()

    def add_group(self, admin_id, group_name):
        command = """INSERT INTO GROUPS (
            user_id, group_name, user_role, createdOn) VALUES(
                '{}','{}','{}','{}') RETURNING * ;
        """.format(admin_id, group_name, "admin", datetime.now())
        self.cursor.execute(command)
        data = self.cursor.fetchone()
        return data

    def search_group(self, id):
        command = """
        SELECT * FROM GROUPS WHERE id = {}
        """.format(id)
        self.cursor.execute(command)
        data = self.cursor.fetchone()
        return data

    def delete_group(self, id):
        """delete message."""
        command = "DELETE FROM GROUPS CASCADE WHERE id = '%s'" % (id)
        self.cursor.execute(command)
        return "message deleted"

    def add_user_to_group(self, email, group_id):
        command = """INSERT INTO members (
            email, group_id, user_role, createdOn) VALUES(
                '{}','{}','{}','{}') RETURNING * ;
        """.format(email, group_id, "user", datetime.now())
        self.cursor.execute(command)
        data = self.cursor.fetchone()
        return data

    def delete_user_from_group(self, group_id, user_id):
        """delete user from group"""
        command = "DELETE FROM MEMBERS WHERE group_id = '%s' and user_id = '%s'" % (
            group_id, user_id)
        self.cursor.execute(command)
        return "user deleted"

    def send_message_to_group(self, group_id, subject, message, parentMessageID, status, read):
        """add message to a group"""
        command = """INSERT INTO GROUP_MESSAGES (
            group_id, subject, message, parentMessageID, status, read, createdon)
        VALUES('{}', '{}','{}', '{}', '{}', '{}','{}') RETURNING *;
        """.format(
            group_id, subject, message, parentMessageID, status, read, datetime.now())
        self.cursor.execute(command)
        data = self.cursor.fetchone()
        return data

    def get_all_groups(self):
        command = """
        SELECT * FROM GROUPS""".format()
        self.cursor.execute(command)
        data = self.cursor.fetchall()
        return data

    def admin_update_group_name(self, group_id, group_name):
        """Admin updates a group name."""
        command = """UPDATE GROUPS SET group_name = %s WHERE id= %s RETURNING * ;
        """
        self.cursor.execute(command,(group_name, group_id))
        data = self.cursor.fetchone()
        return data

    
      


