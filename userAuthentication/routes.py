from flask import jsonify, request, Blueprint

from userAuthentication import UserAuthentication as userAuth


auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/userAuthentication/login', methods=['POST'])
def login():
    # Validate json
    if not request.is_json:
        return jsonify({'success': False, 'message': 'Missing JSON in request'}), 400
    
    if not request.json['username']:
        return jsonify({'success': False, 'message': 'Missing username parameter'}), 400
    
    if not request.json['password']:
        return jsonify({'success': False, 'message': 'Missing password parameter'}), 400
    
    # Try to login
    auth = userAuth.UserAuthentication()
    login_success = auth.login(request.json['username'], request.json['password'])
    if not login_success:
        return jsonify({'success': False, 'message': 'Invalid username or password'}), 401
    
    # Generate JWT
    jwt = auth.generateJwt()

    return jsonify({'success': True, 'jwt': jwt}), 200

