import unittest
import json
from app.views import app


class EmailsTest(unittest.TestCase):
    """Tests for Emails."""

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_create_user_account(self):
        """test add new user."""
        user = {
            "id": 1,
            "email": "kyakuluahmed@gmail.com",
            "firstname": "ahmed",
            "lastname": "kyakus",
            "password": "ch1988"
        }
        response = self.app.post('/api/v1/users/signup', json=user)
        self.assertEqual(response.status_code, 201)

    def test_create_user_account_already_exists(self):
        """test add new user exists."""
        user = {
            "id": 1,
            "email": "kyakuluahmed@gmail.com",
            "firstname": "ahmed",
            "lastname": "kyakus",
            "password": "ch1988"
        }
        response = self.app.post('/api/v1/users/signup', json=user)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            json.loads(
                response.data.decode('utf-8')).get('message'), "user registered already"
                )

    def test_create_user_account_with_invalid_email(self):
        """test add new user with invalid email."""
        user = {
            "id": 1,
            "email": "kyakuluahmedgmail.com",
            "firstname": "ahmed",
            "lastname": "kyakus",
            "password": "ch1988"
        }
        response = self.app.post('/api/v1/users/signup', json=user)
        self.assertEqual(response.status_code, 400)

    def test_add_create_user_account_missing_firstname(self):
        """test add new user missing firstname field."""
        user = {
            "id": 1,
            "email": "kyakuluahmed@gmail.com",
            "firstname": "",
            "lastname": "kyakus",
            "password": "ch1988"
        }
        response = self.app.post('/api/v1/users/signup', json=user)
        self.assertEqual(response.status_code, 400)

    def test_add_create_user_account_with_short_password(self):
        """test add new user with password too short."""
        user = {
            "id": 1,
            "email": "kyakuluahmed@gmail.com",
            "firstname": "ahmed",
            "lastname": "kyakus",
            "password": "ch"
        }
        response = self.app.post('/api/v1/users/signup', json=user)
        self.assertEqual(response.status_code, 400)

    def test_user_login(self):
        """Test successful login"""
        user = {
            "firstname": "joel",
            "lastname": "joe",
            "email": "kyakusahmed@out.com",
            "password": "1988ch"
        }
        self.app.post('/api/v1/users', json=user)
        user1 = {
            "email": "kyakusahmed@out.com",
            "password": "1988ch"
        }
        response = self.app.post('/api/v1/users/login', json=user1)
        self.assertEqual(response.status_code, 200)

    def test_user_login_with_invalid_email(self):
        """Test successful login"""
        user = {
            "firstname": "joel",
            "lastname": "joe",
            "email": "kyakusahmed@out.com",
            "password": "1988ch"
        }
        self.app.post('/api/v1/users', json=user)
        user1 = {
            "email": "kyakusahmed@out",
            "password": "1988ch"
        }
        response = self.app.post('/api/v1/users/login', json=user1)
        self.assertEqual(response.status_code, 400)
        assert json.loads(response.data)['errors']['message'] == "invalid email"
        assert json.loads(response.data)['errors']['field'] == "email"

    def test_user_login_with_short_password(self):
        """Test login with short password"""
        user = {
            "firstname": "joel",
            "lastname": "joe",
            "email": "kyakusahmed@out.com",
            "password": "1988ch"
        }
        self.app.post('/api/v1/users', json=user)
        user1 = {
            "email": "kyakusahmed@out.com",
            "password": "19"
        }
        response = self.app.post('/api/v1/users/login', json=user1)
        self.assertEqual(response.status_code, 400)
        assert json.loads(response.data)['errors']== "password should be atleast five characters"


    def test_user_login_with_field_missing(self):
        """Test login with short password"""
        user = {
            "firstname": "joel",
            "lastname": "joe",
            "email": "kyakusahmed@out.com",
            "password": "1988ch"
        }
        self.app.post('/api/v1/users', json=user)
        user1 = {
            "email": "kyakusahmed@out.com",
            "password": ""
        }
        response = self.app.post('/api/v1/users/login', json=user1)
        self.assertEqual(response.status_code, 400)
        assert json.loads(response.data)['errors']['message']== "password is required"

    def test_send_email_to_user(self):
        """send an email to a user"""
        email = {
            "subject": "ASKJBFIWBFA",
            "message": "UIWQUKAJSFIUQNSA",
            "status": "sent",
            "sender_id": 3,
            "receiver_id": 1
        }
        response = self.app.post('/api/v1/emails/user', json=email)
        self.assertEqual(response.status_code, 201)
        self.assertIsInstance(json.loads(response.data.decode('utf-8')).get('data'), list)
    
    def test_send_email_to_user_doesnot_exist(self):
        """send an email to a user who does not exist"""
        email = {
            "subject": "ASKJBFIWBFA",
            "message": "UIWQUKAJSFIUQNSA",
            "status": "sent",
            "sender_id": 1,
            "receiver_id": 3
        }
        response = self.app.post('/api/v1/emails/user', json=email)
        self.assertEqual(response.status_code, 200)

    def test_send_email_to_user_with_missing_field(self):
        """send an email to a user with a missing field"""
        email = {
            "subject": "",
            "message": "UIWQUKAJSFIUQNSA",
            "status": "sent",
            "sender_id": "hjy",
            "receiver_id": 1
        }
        response = self.app.post('/api/v1/emails/user', json=email)
        self.assertEqual(response.status_code, 400)
        
        
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