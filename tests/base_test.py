from .import user_register, admin_login, user_login
from app import app
import unittest
import json
from app.models.migration import Migration


class BaseTest(unittest.TestCase):
    
    def setUp(self):
        self.migration = Migration()
        self.app = app.test_client()
        
    def return_admin_token(self):
        response = self.app.post('/api/v1/auth/login', json=admin_login)
        return json.loads(response.data)['data'][0]['access_token']

    def return_user_token(self):
        """user token."""
        self.app.post('/api/v1/auth/signup', json=user_register)
        response = self.app.post('/api/v1/auth/login', json=user_login)
        return json.loads(response.data)['data'][0]['access_token']