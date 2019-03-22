import unittest
import json
from app.views import app


class EmailsTest(unittest.TestCase):
    """Tests for Emails."""

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
    
   

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

   