import unittest
import json
from app import app


class MessagesTest(unittest.TestCase):
    """Tests for Emails."""

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_send_message_to_user_with_same_sender_id(self):
        """send an email to a user"""
        message_info = {
            "subject": "ASKJBFIWBFA", "message": "UIWQUKAJSFIUQNSA",
            "status": "sent","sender_id": 1, "receiver_id": 1, "read": False
        }
        response = self.app.post('/api/v1/messages', json=message_info)
        print(response)
        self.assertEqual(response.status_code, 400)
        assert json.loads(response.data)['message']== "you can not send an email to yourself"

    def test_send_message_to_user_with_sender_id_that_is_not_integer(self):
        message_info = {
            "subject": "ASKJBFIWBFA", "message": "UIWQUKAJSFIUQNSA",
            "status": "sent","sender_id": "abse", "receiver_id": "miun", "read": False
        }
        response = self.app.post('/api/v1/messages', json=message_info)
        self.assertEqual(response.status_code, 400)
    
    def test_send_email_to_user_doesnot_exist(self):
        """send an email to a user who does not exist"""
        email = {
            "subject": "ASKJBFIWBFA",
            "message": "UIWQUKAJSFIUQNSA",
            "status": "sent",
            "sender_id": 1,
            "receiver_id": 3,
            "read": False
        }
        response = self.app.post('/api/v1/messages', json=email)
        self.assertEqual(response.status_code, 404)
        assert json.loads(response.data)['message']== "user does not exist"


    def test_send_message_to_user_with_missing_field(self):
        """send an email to a user with a missing field"""
        message_info = {
            "subject": "",
            "message": "UIWQUKAJSFIUQNSA",
            "status": "sent",
            "sender_id": "hjy",
            "receiver_id": 1
        }
        response = self.app.post('/api/v1/messages', json=message_info)
        self.assertEqual(response.status_code, 400)
        
        
    def test_get_specific_user_message(self):
        """test get specific user email"""
        message_info = {
            "subject": "whjtkry",
            "message": "UIWQUKAJSFIUQNSA",
            "status": "sent",
            "sender_id": 2,
            "receiver_id": 1,
            "read": False
        }
        self.app.post('/api/v1/messages', json=message_info)
        response = self.app.get('/api/v1/messages/1')
        self.assertEqual(response.status_code, 200)
        
        
    def test_get_all_user_unread_emails(self):
        """test user gets unread emails"""
        message_info = {
            "subject": "ppmsnsSS",
            "message": "UIWQUKAJSFIUQNSA",
            "status": "sent",
            "sender_id": 2,
            "receiver_id": 1,
            "read": False
        }
        self.app.post('/api/v1/messages', json=message_info)
        response = self.app.get('/api/v1/messages/unread')
        self.assertEqual(response.status_code, 200)


    def test_delete_user_message(self):
        """test delete user message"""
        message_info = {
            "subject": "ppmsnsSS",
            "message": "UIWQUKAJSFIUQNSA",
            "status": "sent",
            "sender_id": 1,
            "receiver_id": 2,
            "read": False
        }
        self.app.post('/api/v1/messages', json=message_info)
        response = self.app.delete('/api/v1/messages/delete/1')
        self.assertEqual(response.status_code, 200)


    def test_delete_user_message_doesnot_exist(self):
        """test delete user message"""
        response = self.app.delete('/api/v1/messages/delete/1000')
        assert json.loads(
            response.data)['deleted_message'] == []


    def test_get_user_sent_messages(self):
        """test get sent messages by a user"""
        message_info = {
            "subject": "ppmsnsSS",
            "message": "UIWQUKAJSFIUQNSA",
            "status": "sent",
            "sender_id": 2,
            "receiver_id": 1,
            "read": False
        }
        self.app.post('/api/v1/messages', json=message_info)
        response = self.app.get('/api/v1/messages/sent')
        print(response)
        self.assertEqual(response.status_code, 200)


    def test_get_user_received_messages(self):
        """test to get users received messages"""
        message_info = {
            "subject": "ppmsnsSS",
            "message": "UIWQUKAJSFIUQNSA",
            "status": "sent",
            "sender_id": 2,
            "receiver_id": 1,
            "read": False
        }
        self.app.post('/api/v1/messages', json=message_info)
        response = self.app.get('/api/v1/messages/received')
        print(response)
        self.assertEqual(response.status_code, 200)






