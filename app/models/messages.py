from app.models.db_conn import DatabaseConnection
from datetime import datetime
from flask import json, jsonify
import psycopg2


class Messages(DatabaseConnection):

    def __init__(self):
        super().__init__()

    def add_message(self, subject, message, parentMessageID, status, sender_id, receiver_id, read):
        command = """INSERT INTO MESSAGES (subject, message, parentMessageID, status, user_id, receiver_id, read, createdon)
        VALUES('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}') RETURNING*;
        """.format(subject, message, parentMessageID, status, sender_id, receiver_id, read, datetime.now())
        self.cursor.execute(command)
        data = self.cursor.fetchone()
        return data

    def get_user_received_messages(self, receiver_id, status, read):
        command = """
        SELECT * FROM MESSAGES WHERE receiver_id = {} AND status = 'read' or read = False 
        """.format(receiver_id, status, read)
        self.cursor.execute(command)
        data = self.cursor.fetchall()
        return data

    def get_sent_messages(self, status, user_id):
        try:
            command = """
            SELECT * FROM MESSAGES WHERE status = 'sent' and user_id = {}
            """.format(user_id, status)
            self.cursor.execute(command)
            data = self.cursor.fetchall()
            return data
        except psycopg2.IntegrityError as identifier:
            message = ("messages dont exist")
            return message

    def delete_message(self, message_id):
        command = "DELETE FROM MESSAGES CASCADE WHERE message_id = '%s'" % (
            message_id)
        self.cursor.execute(command)
        return "message deleted"

    def search_message(self, message_id):
        command = """
        SELECT * FROM MESSAGES WHERE message_id = {}
        """.format(message_id)
        self.cursor.execute(command)
        data = self.cursor.fetchone()
        return data

    def get_data(self, receiver_id):
        command =  "SELECT row_to_json(messages) FROM messages WHERE receiver_id='%s'" % (receiver_id)
        self.cursor.execute(command, (receiver_id))
        result = self.cursor.fetchone()
        if not result:
            return "message not saved"
        return result
