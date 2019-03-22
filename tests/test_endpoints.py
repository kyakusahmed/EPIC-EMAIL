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
