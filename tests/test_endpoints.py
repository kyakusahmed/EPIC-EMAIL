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

