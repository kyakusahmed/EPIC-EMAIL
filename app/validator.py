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
                elif x.strip() == 'email' and not bool(match(r"^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$", input[x])):
                    msg = 'invalid email'
                    return ({'field': x, 'message': msg})
                elif x.strip() == 'password' and len(input[x].strip()) < 5:
                    message = 'password should be atleast five characters'
                    return message