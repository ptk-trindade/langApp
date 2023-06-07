from flask import jsonify, request, Blueprint

from userAuthentication.userAuthentication import UserAuthentication
from card.card import Card
from models.comment import Comment


card_bp = Blueprint('card', __name__)

@card_bp.route('/card/<card_id>/comment', methods=['GET'])
def getComments(card_id: int):
    
    # TODO: Get comments

    # Return the comments
    data = []
    return jsonify(data)


@card_bp.route('/card/comment', methods=['POST'])
def postAddComment():
    # Validate json
    if not request.is_json:
        return jsonify({'success': False, 'message': 'Missing JSON in request'}), 400
    
    if not request.json['card_id']:
        return jsonify({'success': False, 'message': 'Missing card_id parameter'}), 400
    
    if not request.json['user_id']:
        return jsonify({'success': False, 'message': 'Missing user_id parameter'}), 400
    
    if not request.json['text']:
        return jsonify({'success': False, 'message': 'Missing text parameter'}), 400
    
    if not request.json['parent_comment_id']:
        pass

    # TODO: Authenticate the User (by JWT)
    auth = UserAuthentication()
    bearer = request.headers.get('Authorization')
    user_id = auth.authenticateJwt(bearer)

    # TODO: Add comment
    card = Card(card_id)

    comment: Comment = addComment(user_id, text, parent_comment_id)
    # Return the created comment
    data = []
    return jsonify(data)

