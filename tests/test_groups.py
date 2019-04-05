from tests.base_test import BaseTest
import json


class GroupTest(BaseTest):
    """Tests for groups."""

    def test_create_group(self):
        """test create new group"""
        token = self.return_admin_token()
        group_info = {
            "group_name": "finance",
	        "user_role": "admin"
        }
        response = self.app.post(
            '/api/v1/groups', headers={
                "Authorization": "Bearer " + token}, json=group_info)
        self.assertEqual(response.status_code, 201)

    def test_delete_group_not_found(self):
        """test delete group"""
        token = self.return_user_token()
        group_info = {
            "group_name": "finance",
	        "user_role": "admin"
        }
        self.app.post(
            '/api/v1/groups', headers={
                "Authorization": "Bearer " + token}, json=group_info)
        response = self.app.delete(
            '/api/v1/groups/delete/1', headers={
                "Authorization": "Bearer " + token})
        print(response)        
        self.assertEqual(response.status_code, 404)

    def test_add_user_to_group(self):
        """test add user to a group"""
        token = self.return_admin_token()
        group_info = {
            "group_name": "finance",
	        "user_role": "admin"
        }
        self.app.post('/api/v1/groups', headers={"Authorization": "Bearer " + token}, json=group_info)
        user_info = {
           
	        "user_role": "member"
        }
        response = self.app.post('/api/v1/groups/1/users', headers={"Authorization": "Bearer " + token}, json=user_info)
        self.assertEqual(response.status_code, 201)


    def test_delete_user_from_group(self):
        """test delete user from group"""
        token = self.return_user_token()
        group_info = {
            "group_name": "finance",
	        "user_role": "admin"
        }
        self.app.post('/api/v1/groups', headers={"Authorization": "Bearer " + token}, json=group_info)
        user_info = {
            "user_id": 3,
	        "user_role": "member"
        }
        self.app.post('/api/v1/groups/1/users', headers={"Authorization": "Bearer " + token}, json=user_info)
        response = self.app.delete(
            '/api/v1/groups/1/users/1', headers={
                "Authorization": "Bearer " + token})
        self.assertEqual(response.status_code, 200)

