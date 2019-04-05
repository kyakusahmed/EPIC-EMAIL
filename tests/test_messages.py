from tests.base_test import BaseTest
import json


class MessagesTest(BaseTest):
    """Tests for messages."""

    def test_send_message_to_user_with_user_id_that_is_not_integer(self):
        """test sender_id is not integer"""
        token = self.return_user_token()
        message_info = {
            "subject": "ASKJBFIWBFA", "message": "UIWQUKAJSFIUQNSA", "parentMessageId": 0,
            "status": "sent", "user_id": "abse", "receiver_email": "kyausahmed@outlook.com",
            "read": False
        }
        response = self.app.post(
            '/api/v1/messages', headers={
                "Authorization": "Bearer " + token}, json=message_info)
        self.assertEqual(response.status_code, 404)

    def test_send_message_to_user_doesnot_exist(self):
        """send an email to a user who does not exist"""
        token = self.return_user_token()
        message_info = {
            "subject": "ASKJBFIWBFA",
            "message": "UIWQUKAJSFIUQNSA",
            "status": "sent",
            "user_id": 1000,
            "receiver_email": "kyakutatat.gmail.you",
            "read": False
        }
        response = self.app.post(
            '/api/v1/messages', headers={
                "Authorization": "Bearer " + token}, json=message_info)
        self.assertEqual(response.status_code, 404)
        assert json.loads(response.data)['message'] == "Recipient does not exist"

    def test_send_message_to_user_with_missing_field(self):
        """send an email to a user with a missing field"""
        token = self.return_user_token()
        message_info = {
            "subject": "",
            "message": "UIWQUKAJSFIUQNSA",
            "parentMessageID": 1,
            "status": "sent",
            "receiver_id": 1
        }
        response = self.app.post(
            '/api/v1/messages', headers={
                "Authorization": "Bearer " + token}, json=message_info)
        self.assertEqual(response.status_code, 400)

    def test_get_specific_user_message(self):
        """test get specific user email"""
        token = self.return_user_token()
        message_info = {
            "subject": "whjtkry",
            "message": "UIWQUKAJSFIUQNSA",
            "parentMessageID": 0,
            "status": "sent",
            "receiver_email": "kyakusahmed@gmail.com"
        }
        self.app.post(
            '/api/v1/messages', headers={
                "Authorization": "Bearer " + token}, json=message_info)
        response = self.app.get(
            '/api/v1/messages/2', headers={
                "Authorization": "Bearer " + token})
        self.assertEqual(response.status_code, 404)

    def test_get_all_user_unread_emails(self):
        """test user gets unread emails"""
        token = self.return_user_token()
        message_info = {
            "subject": "ppmsnsSS",
            "message": "UIWQUKAJSFIUQNSA",
            "parentMessageID": 1,
            "status": "sent",
            "receiver_id": 1,
            "read": False
        }
        self.app.post(
            '/api/v1/messages', headers={
                "Authorization": "Bearer " + token}, json=message_info)
        response = self.app.get(
            '/api/v1/messages/unread', headers={
                "Authorization": "Bearer " + token})
        self.assertEqual(response.status_code, 200)

    # def test_delete_user_message(self):
    #     """test delete user message"""
    #     token = self.return_user_token()
    #     message_info = {
    #         "subject": "ppmsnsSS",
    #         "message": "UIWQUKAJSFIUQNSA",
    #         "parentMessageID": 1,
    #         "status": "sent",
    #         "receiver_id": 2
    #     }
    #     self.app.post(
    #         '/api/v1/messages', headers={
    #             "Authorization": "Bearer " + token}, json=message_info)
    #     response = self.app.delete('/api/v1/messages/delete/1')
    #     self.assertEqual(response.status_code, 200)

    # def test_delete_user_message_doesnot_exist(self):
    #     """test delete user message"""
    #     token = self.return_user_token()
    #     response = self.app.delete(
    #         '/api/v1/messages/delete/1000', headers={
    #             "Authorization": "Bearer " + token})
    #     assert json.loads(
    #         response.data)['message'] == "message not found"

    def test_get_user_sent_messages(self):
        """test get sent messages by a user"""
        token = self.return_user_token()
        message_info = {
            "subject": "ppmsnsSS",
            "message": "UIWQUKAJSFIUQNSA",
            "status": "sent",
            "sender_id": 2,
            "receiver_id": 1,
            "read": False
        }
        self.app.post(
            '/api/v1/messages', headers={
                "Authorization": "Bearer " + token}, json=message_info)
        response = self.app.get(
            '/api/v1/messages/sent', headers={
                "Authorization": "Bearer " + token})
        self.assertEqual(response.status_code, 200)

    def test_get_user_received_messages(self):
        """test to get users received messages"""
        token = self.return_user_token()
        message_info = {
            "subject": "ppmsnsSS",
            "message": "UIWQUKAJSFIUQNSA",
            "status": "sent",
            "sender_id": 2,
            "receiver_id": 1,
            "read": False
        }
        self.app.post(
            '/api/v1/messages', headers={
                "Authorization": "Bearer " + token}, json=message_info)
        response = self.app.get(
            '/api/v1/messages/received', headers={
                "Authorization": "Bearer " + token})
        self.assertEqual(response.status_code, 200)
