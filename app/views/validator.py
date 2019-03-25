"""validate inputs"""
from flask import jsonify, request
from re import match

input_data = []


class Validation:
    """class for validating data"""
    def __init__(self):
        self.input_data = input_data

    def input_data_validation(self, input_data):
        """Search for x and check if input is an empty string."""
        for x in input_data:
            input = request.get_json()
            message = x.strip() + ' is required'
            if not input[x]:
                return {'field': x, 'message': message}
            elif x.strip() == 'password' and len(input[x].strip()) < 5:
                message = 'password should be atleast five characters'
                return message
            elif x.strip() == 'status' and input[x].strip() not in [
                    'sent', 'draft', 'read']:
                message = "Status must be sent, draft or read"
                return message
