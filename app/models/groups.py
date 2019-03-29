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
                '{}','{}','{}','{}') RETURNING *;
        """.format(user_id, group_id, user_role, datetime.now())
        self.cursor.execute(command)
        data = self.cursor.fetchone()
        return data

    def delete_user_from_group(self, group_id, user_id):
        """delete user from group"""
        command = "DELETE FROM MEMBERS WHERE group_id = '%s' and user_id = '%s'" % (
            group_id, user_id)
        self.cursor.execute(command)
        return "user deleted"

    def get_that_group(self, group_name):
        """return group information"""
        command =  "SELECT row_to_json(groups) FROM groups WHERE group_name='%s'" % (group_name)
        self.cursor.execute(command, (group_name))
        result = self.cursor.fetchone()
        if not result:
            return "message not saved"
        return result

    def send_message_to_group(self, group_id, subject, message, parentMessageID, status, read):
        """add message to a group"""
        command = """INSERT INTO GROUP_MESSAGES (
            group_id, subject, message, parentMessageID, status, read, createdon)
        VALUES('{}', '{}','{}', '{}', '{}', '{}','{}')
        """.format(
            group_id, subject, message, parentMessageID, status, read, datetime.now())
        self.cursor.execute(command)

    def get_that_message(self, subject):
        """return group information"""
        command =  "SELECT row_to_json(group_messages) FROM group_messages WHERE subject='%s'" % (subject)
        self.cursor.execute(command, (subject))
        result = self.cursor.fetchone()
        if not result:
            return "message not saved"
        return result

    def get_user(self, user_id):
        """return group information"""
        command =  "SELECT row_to_json(members) FROM members WHERE user_id='%s'" % (user_id)
        self.cursor.execute(command, (user_id))
        result = self.cursor.fetchone()
        if not result:
            return "message not saved"
        return result

    def get_all_groups(self):
        command = """
        SELECT * FROM GROUPS""".format()
        self.cursor.execute(command)
        data = self.cursor.fetchall()
        return data

    
      


