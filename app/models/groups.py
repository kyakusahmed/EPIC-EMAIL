from app.models.db_conn import DatabaseConnection
from datetime import datetime
import psycopg2


class Group(DatabaseConnection):

    def __init__(self):
        super().__init__()

    def add_group(self, admin_id, group_name, user_role):
        command = """INSERT INTO GROUPS (
            user_id, group_name, user_role, createdOn) VALUES(
                '{}','{}','{}','{}')
        """.format(admin_id, group_name, user_role, datetime.now())
        self.cursor.execute(command)
        return "group created"

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

    def add_user_to_group(self, user_id, group_id, user_role):
        command = """INSERT INTO members (
            user_id, group_id, user_role, createdOn) VALUES(
                '{}','{}','{}','{}')
        """.format(user_id, group_id, user_role, datetime.now())
        self.cursor.execute(command)
        return "user added to group"

    def delete_user_from_group(self, group_id, user_id):
        """delete user from group"""
        command = "
        DELETE FROM MEMBERS WHERE group_id = '%s' and user_id = '%s'" % (
            group_id, user_id)
        self.cursor.execute(command)
        return "user deleted"

    # def send_message_to_group(
    #     self, subject, message, parentMessageID,
    #         status, sender_id, receiver_id, read):
    #     """send message to a group"""
