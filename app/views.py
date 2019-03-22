@app.route('/api/v1/emails/user/<int:id>', methods=['POST'])
def send_email_to_user(id):
    """send email to a user."""
    validate_credentials = validator.input_data_validation([
        'subject', 'message', 'sender_id', 'status'])
    if validate_credentials:
        return jsonify({
            "message": 'Validation error',
            "errors": validate_credentials
        }), 400
    data = request.get_json()
    if type(data['sender_id']) is not int:
        return jsonify({
            "data_type_error": "please enter an integer",
            "status": 400
            }), 400
    if data['sender_id'] == id:
        return jsonify({
            "status": 200, "message": "you can not send an email to yourself"}), 200
    user_search = emails.search_user_by_id(id)
    if not user_search:
        return jsonify({
            "status": 404, "message": "user does not exist"
            }), 200
    email_send = emails.send_email(
        data['subject'],
        data["message"],
        data["status"],
        data['sender_id'],
        id
        )
    return jsonify({"data": [email_send], "status": 201}), 201