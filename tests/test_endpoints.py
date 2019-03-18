import unittest
import json
from app.views import app


class EmailsTest(unittest.TestCase):
    """Tests for Emails."""

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

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
        assert json.loads(response.data)['message'] == "Login successful"


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