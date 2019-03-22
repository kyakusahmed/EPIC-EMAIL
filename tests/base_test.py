from . import user_register, user_login
from app.views import app
import unittest
import json

class BaseTest(unittest.TestCase):
    
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True


    def return_user_token(self):
        """user token."""
        self.app.post('/api/v1/users/register', json=user_register)
        response = self.app.post('/api/v1/users/login', json=user_login)
        return json.loads(response.data)['access_token']