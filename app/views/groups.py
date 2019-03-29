from flask import jsonify, request
from app import app
from app.views.auth import User
from app.models.messages import Messages
from app.models.groups import Group
from app.views.validator import Validation
from flasgger import swag_from
from flask_jwt_extended import (jwt_required, get_jwt_identity)

group = Group()
messages = Messages()
user = User()
validator = Validation()



@app.route('/api/v1/groups', methods=['POST'])
@jwt_required
@swag_from('../docs/create_group.yml')
def create_group():
    """send email to an individual."""
    current_user = get_jwt_identity()
    if current_user[6] != "admin":
        return jsonify({"message": "unauthorized access"})
    validate_info = validator.input_data_validation([
        'group_name', 'user_role'
        ])
    if validate_info:
        return jsonify({
            "message": 'Validation error',
            "errors": validate_info
        }), 400
    data = request.get_json()

    role = data['user_role']
    user_roles = ['admin', 'user']
    if role not in user_roles:
        return jsonify({"error": " role {} doesnot exist".format(user_role)}), 200
    send_group = group.add_group(
        current_user[0],
        data['group_name'],
        data['user_role'],
        )
    check_group = group.get_that_group(data['group_name'])
    return jsonify({"group": check_group, "status": 201}), 201


@app.route('/api/v1/groups/<int:id>', methods=['DELETE'])
@jwt_required
@swag_from('../docs/delete_group.yml')
def delete_group(id):
    """delete user's group"""
    current_user = get_jwt_identity()
    if current_user[6] != "admin":
        return jsonify({"status": 401, "message": "unauthorized access"})
    search_group = group.search_group(id)
    if not search_group:
        return jsonify({"status": 404, "group": "unable to find group"}), 404
    deleted_message = [{"message": group.delete_group(id)}]
    return jsonify({
        "data": deleted_message, "status": 200
        }), 200


@app.route('/api/v1/groups/<int:group_id>/users/<int:user_id>', methods=['DELETE'])
@jwt_required
@swag_from('../docs/delete_user_from_group.yml')
def delete_user_from_group(group_id, user_id):
    """delete user's group"""
    current_user = get_jwt_identity()
    if current_user[6] != "admin":
        return jsonify({"status": 401, "message": "unauthorized access"})
    search_group = group.search_group(group_id)
    if not search_group:
        return jsonify({"status": 404, "group": "unable to find group"}), 404
    search_user = user.search_user_by_id(user_id)
    if not search_user:
        return jsonify({"status": 404, "group": "unable to find user"}), 404
    deleted_message = [{"message": group.delete_user_from_group(group_id, user_id)}]
    return jsonify({
        "data": deleted_message, "status": 200
        }), 200


@app.route('/api/v1/groups/<int:id>/users', methods=['POST'])
@jwt_required
@swag_from('../docs/add_user_to_group.yml')
def add_user_to_group(id):
    """send email to an individual."""
    current_user = get_jwt_identity()
    if current_user[6] != "admin":
        return jsonify({"message": "unauthorized access"})
    validate_credentials = validator.input_data_validation(['user_id', 'user_role'])
    if validate_credentials:
        return jsonify({
            "message": 'Validation error',
            "errors": validate_credentials
        }), 400
    data = request.get_json()
    if type(data['user_id']) is not int:
        return jsonify({
            "data_type_error": "please enter an integer",
            "status": 400
            }), 400
    if current_user[0] == data['user_id']:
        return jsonify({
            "status": 400, "message": "you are an administrator of this group"
            }), 400
    check_user = user.search_user_by_id(data['user_id'])
    if not check_user:
        return jsonify({"status": 404, "message": "unable to find user"}), 404        
    group_search = group.search_group(id)
    if not group_search:
        return jsonify({
            "status": 404, "message": "unable to find this group"
            }), 404
    send_message = group.add_user_to_group(
        data['user_id'],
        id,
        data["user_role"]
        )
    get_user = group.get_user(data['user_id'])
    return jsonify({"data": get_user, "status": 201}), 201


@app.route('/api/v1/groups/<int:group_id>/messages', methods=['POST'])
@jwt_required
@swag_from('../docs/send_message_to_group.yml')
def send_message_to_group(group_id):
    """send email to an individual."""
    current_user = get_jwt_identity()
    if current_user[6] != "admin":
        return jsonify({"message": "unauthorized access"})
    validate_credentials = validator.input_data_validation([
        'subject', 'message', 'parentMessageID', 'status'])
    if validate_credentials:
        return jsonify({
            "message": 'Validation error',
            "errors": validate_credentials
        }), 400
    data = request.get_json()
    if type(data['parentMessageID']) is not int:
        return jsonify({
            "data_type_error": "please enter an integer",
            "status": 400
            }), 400

    search_group = group.search_group(group_id)
    if not search_group:
        return jsonify({
            "status": 404, "message": "unable to find group"
            }), 404
    add_group = group.send_message_to_group(
        group_id,
        data['subject'],
        data["message"],
        data['parentMessageID'],
        data["status"],
        False
        )
    message_info = group.get_that_message(data['subject'])
    return jsonify({"message": message_info, "status": 201}), 201


@app.route('/api/v1/groups', methods=['GET'])
@jwt_required
@swag_from('../docs/get_user_received_emails.yml')
def get_all_groups():
    """fetch all user received messages"""
    current_user = get_jwt_identity()
    if current_user[6] != "admin":
        return jsonify({"message": "unauthorized access"})
    all_groups = group.get_all_groups()
    groups = []
    for key in range(len(all_groups)):
        groups.append({
            'id': all_groups[key][0],
            'user_id':all_groups[key][1],
            'group_name': all_groups[key][2],
            'user_role': all_groups[key][3],
            'createdon': all_groups[key][4]
        })
    return jsonify({"status": 200, "groups": groups}), 200
