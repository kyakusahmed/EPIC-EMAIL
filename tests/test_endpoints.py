import unittest
import json
from app.views import app
from .base_test import BaseTest


class EmailsTest(BaseTest):
    """Tests for Emails."""

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

