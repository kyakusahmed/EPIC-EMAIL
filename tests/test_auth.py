import unittest
import json
from app import app


class AuthTest(unittest.TestCase):
    """Tests for Emails."""

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        self.create_user = {
            "first_name": "ahmad",
            "last_name": "kyakus",
            "email": "kyakusahmed@gmail.com",
            "password": "ch1988"
            }

    def test_index(self):
        """test open route"""
        response = self.app.get('/')
        assert response.status_code == 200
        assert json.loads(response.data)['message'] == "welcome to Epic Email."

    def test_create_user_account(self):
        """test add new user."""
        user_info = {
            "id": 1,
            "email": "kyakuluahmed@gmail.com",
            "firstname": "ahmed",
            "lastname": "kyakus",
            "password": "ch1988"
        }
        response = self.app.post('/api/v1/auth/signup', json=user_info)
        self.assertEqual(response.status_code, 201)

    def test_create_user_account_already_exists(self):
        """test add new user exists."""
        user_info = {
            "id": 1,
            "email": "kyakuluahmed@gmail.com",
            "firstname": "ahmed",
            "lastname": "kyakus",
            "password": "ch1988"
        }
        response = self.app.post('/api/v1/auth/signup', json=user_info)
        self.assertEqual(response.status_code, 200)

    def test_create_user_account_with_invalid_email(self):
        """test add new user with invalid email."""
        user_info = {
            "id": 1,
            "email": "kyakuluahmedgmail.",
            "firstname": "ahmed",
            "lastname": "kyakus",
            "password": "ch1988"
        }
        response = self.app.post('/api/v1/auth/signup', json=user_info)
        self.assertEqual(response.status_code, 400)

    def test_create_user_account_missing_firstname(self):
        """test add new user missing firstname field."""
        user_info = {
            "id": 1,
            "email": "kyakuluahmed@gmail.com",
            "firstname": "",
            "lastname": "kyakus",
            "password": "ch1988"
        }
        response = self.app.post('/api/v1/auth/signup', json=user_info)
        self.assertEqual(response.status_code, 400)

    def test_create_user_account_with_short_password(self):
        """test add new user with password too short."""
        user_info = {
            "id": 1,
            "email": "kyakuluahmed@gmail.com",
            "firstname": "ahmed",
            "lastname": "kyakus",
            "password": "ch"
        }
        response = self.app.post('/api/v1/auth/signup', json=user_info)
        self.assertEqual(response.status_code, 400)

    def test_signin_user(self):
        """Test successful login"""
        user_info = {
            "firstname": "joel",
            "lastname": "joe",
            "email": "kyakusahmed@out.com",
            "password": "1988ch"
        }
        self.app.post('/api/v1/auth/signup', json=user_info)
        user_info = {
            "email": "kyakusahmed@out.com",
            "password": "1988ch"
        }
        response = self.app.post('/api/v1/auth/login', json=user_info)
        self.assertEqual(response.status_code, 200)

    def test_signin_user_with_wrong_password_or_email(self):
        """Test successful login"""
        user_info = {
            "firstname": "joel",
            "lastname": "joe",
            "email": "kyakusahmed@out.com",
            "password": "1988ch"
        }
        self.app.post('/api/v1/auth/signup', json=user_info)
        user_info = {
            "email": "kyakusahd@outlook.com",
            "password": "19ch88"
        }
        response = self.app.post('/api/v1/auth/login', json=user_info)
        self.assertEqual(response.status_code, 200)

    def test_siginin_user_with_short_password(self):
        """Test login with short password"""
        user_info = {
            "firstname": "joel",
            "lastname": "joe",
            "email": "kyakusahmed@out.com",
            "password": "1988ch"
        }
        self.app.post('/api/v1/auth/signup', json=user_info)
        user_info = {
            "email": "kyakusahmed@out.com",
            "password": "19"
        }
        response = self.app.post('/api/v1/auth/login', json=user_info)
        self.assertEqual(response.status_code, 400)
        assert json.loads(
            response.data)[
                'errors'] == "password should be atleast five characters"

    def test_sigin_user_with_field_missing(self):
        """Test login with short password"""
        user_info = {
            "firstname": "joel",
            "lastname": "joe",
            "email": "kyakusahmed@out.com",
            "password": "1988ch"
        }
        self.app.post('/api/v1/auth/signup', json=user_info)
        user_info = {
            "email": "kyakusahmed@out.com",
            "password": ""
        }
        response = self.app.post('/api/v1/auth/login', json=user_info)
        self.assertEqual(response.status_code, 400)
        assert json.loads(
            response.data)['errors']['message'] == "password is required"
