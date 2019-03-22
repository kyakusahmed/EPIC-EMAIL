import unittest
import json
from app.views import app


class EmailsTest(unittest.TestCase):
    """Tests for Emails."""

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        
        
    def test_add_new_user(self):
        """test add new user."""
        user = {
            "id": 1,
            "email": "kyakuluahmed@gmail.com",
            "firstname": "ahmed",
            "lastname": "kyakus",
            "password": "ch1988"
        }
        response = self.app.post('/api/v1/users', json=user)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(
            json.loads(
                response.data.decode
                ('utf-8')).get('data')[0]['message'],
                "user registration successful")

    def test_add_new_user_already_exists(self):
        """test add new user exists."""
        user = {
            "id": 1,
            "email": "kyakuluahmed@gmail.com",
            "firstname": "ahmed",
            "lastname": "kyakus",
            "password": "ch1988"
        }
        response = self.app.post('/api/v1/users', json=user)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            json.loads(
                response.data.decode('utf-8')).get('message'), "user registered already"
                )

    def test_add_new_user_with_invalid_email(self):
        """test add new user with invalid email."""
        user = {
            "id": 1,
            "email": "kyakuluahmedgmail.com",
            "firstname": "ahmed",
            "lastname": "kyakus",
            "password": "ch1988"
        }
        response = self.app.post('/api/v1/users', json=user)
        self.assertEqual(response.status_code, 400)

    def test_add_new_user_missing_firstname(self):
        """test add new user missing firstname field."""
        user = {
            "id": 1,
            "email": "kyakuluahmed@gmail.com",
            "firstname": "",
            "lastname": "kyakus",
            "password": "ch1988"
        }
        response = self.app.post('/api/v1/users', json=user)
        self.assertEqual(response.status_code, 400)

    def test_add_new_user_with_short_password(self):
        """test add new user with password too short."""
        user = {
            "id": 1,
            "email": "kyakuluahmed@gmail.com",
            "firstname": "ahmed",
            "lastname": "kyakus",
            "password": "ch"
        }
        response = self.app.post('/api/v1/users', json=user)
        self.assertEqual(response.status_code, 400)

      def test_send_email_to_user(self):
        """send an email to a user"""
        email = {
            "subject": "ASKJBFIWBFA",
            "message": "UIWQUKAJSFIUQNSA",
            "status": "sent",
            "sender_id": 3
        }
        response = self.app.post('/api/v1/emails/user/1', json=email)
        self.assertEqual(response.status_code, 201)
        self.assertIsInstance(json.loads(response.data.decode('utf-8')).get('data'), list)
    
    def test_send_email_to_user_doesnot_exist(self):
        """send an email to a user who does not exist"""
        email = {
            "subject": "ASKJBFIWBFA",
            "message": "UIWQUKAJSFIUQNSA",
            "status": "sent",
            "sender_id": "hjy"
        }
        response = self.app.post('/api/v1/emails/user/1000', json=email)
        self.assertEqual(response.status_code, 400)

    def test_send_email_to_user_with_missing_field(self):
        """send an email to a user with a missing field"""
        email = {
            "subject": "",
            "message": "UIWQUKAJSFIUQNSA",
            "status": "sent",
            "sender_id": "hjy"
        }
        response = self.app.post('/api/v1/emails/user/1', json=email)
        self.assertEqual(response.status_code, 400)
          
         
    def test_get_all_inbox_emails(self):
        token = self.return_user_token()
        response = self.app.get('/api/v1/email/inbox/1', headers={"Authorization": "Bearer " + token})
        self.assertEqual(response.status_code, 200)

    def test_get_all_user_sent_emails(self):
        """test get user sent emails"""
        email = {
            "subject": "",
            "message": "UIWQUKAJSFIUQNSA",
            "status": "sent",
            "sender_id": 2
        }
        self.app.post('/api/v1/emails/user/1', json=email)
        response = self.app.delete('/api/v1/emails/user/sent/2')
        self.assertEqual(response.status_code, 200)
        
        
     def test_get_specific_user_email(self):
        """test get specific user email"""
        email = {
            "subject": "",
            "message": "UIWQUKAJSFIUQNSA",
            "status": "sent",
            "sender_id": 2
        }
        self.app.post('/api/v1/emails/user/1', json=email)
        response = self.app.get('/api/v1/emails/specific-user/2')
        self.assertEqual(response.status_code, 200)
        
        
     def test_get_all_user_unread_emails(self):
        """test user gets unread emails"""
        email = {
            "subject": "",
            "message": "UIWQUKAJSFIUQNSA",
            "status": "sent",
            "sender_id": 2
        }
        self.app.post('/api/v1/emails/user/1', json=email)
        response = self.app.get('/api/v1/emails/user/unread/1')
        self.assertEqual(response.status_code, 200)