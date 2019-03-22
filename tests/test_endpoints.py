    def test_send_email_to_user(self):
        """send an email to a user"""
        email = {
            "subject": "ASKJBFIWBFA",
            "message": "UIWQUKAJSFIUQNSA",
            "status": "sent",
            "sender_id": 3
        }
        response = self.app.post('/api/v1/emails/user/1', json=email)
        self.assertEqual(response.status_code, 201)
        self.assertIsInstance(json.loads(response.data.decode('utf-8')).get('data'), list)
    
    def test_send_email_to_user_doesnot_exist(self):
        """send an email to a user who does not exist"""
        email = {
            "subject": "ASKJBFIWBFA",
            "message": "UIWQUKAJSFIUQNSA",
            "status": "sent",
            "sender_id": "hjy"
        }
        response = self.app.post('/api/v1/emails/user/1000', json=email)
        self.assertEqual(response.status_code, 400)

    def test_send_email_to_user_with_missing_field(self):
        """send an email to a user with a missing field"""
        email = {
            "subject": "",
            "message": "UIWQUKAJSFIUQNSA",
            "status": "sent",
            "sender_id": "hjy"
        }
        response = self.app.post('/api/v1/emails/user/1', json=email)
        self.assertEqual(response.status_code, 400)