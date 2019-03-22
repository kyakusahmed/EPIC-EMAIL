  def test_delete_user_emails(self):
        """test delete user emails"""
        email = {
            "subject": "",
            "message": "UIWQUKAJSFIUQNSA",
            "status": "sent",
            "sender_id": 2
        }
        self.app.post('/api/v1/emails/user/1', json=email)
        response = self.app.delete('/api/v1/emails/user/delete/1')
        self.assertEqual(response.status_code, 200)