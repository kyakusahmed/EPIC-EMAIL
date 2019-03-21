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
        assert json.loads(
            response.data)['errors']['message'] == "invalid email"

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
        assert json.loads(
            response.data)['errors'] == "password should be atleast five characters"

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