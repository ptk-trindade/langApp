from flask import jsonify, request, Blueprint

from userAuthentication.userAuthentication import UserAuthentication
from models.card import Card
from cardComment.cardComment import CardComment
from models.comment import Comment


card_bp = Blueprint('card', __name__)

@card_bp.route('/cardComment/<card_id>', methods=['GET'])
def getComments(card_id: int): # list[Comment]
    
    # TODO: Get comments
    card = Card(card_id)
    comments = card.getComments()

    # Return the comments
    data = comments.toJson()
    return jsonify(data)


@card_bp.route('/cardComment', methods=['POST'])
def postAddComment():
    # Validate json
    if not request.is_json:
        return jsonify({'success': False, 'message': 'Missing JSON in request'}), 400
    
    obrigatory_fields = ['card_id', 'user_id', 'text']
    for field in obrigatory_fields:
        if field not in request.json:
            return jsonify({'success': False, 'message': f'Missing {field} parameter'}), 400

    card_id = request.json['card_id']
    user_id = request.json['user_id']
    text = request.json['text']
    parent_comment_id = None
    if 'parent_comment_id' in request.json:
        parent_comment_id = request.json['parent_comment_id']

    # TODO: Authenticate the User (by JWT)
    auth = UserAuthentication()
    bearer = request.headers.get('Authorization')
    user_id = auth.authenticateJwt(bearer)

    if user_id == 0:
        return jsonify({'success': False, 'message': 'Invalid JWT'}), 400
    

    card = CardComment(card_id)

    comment: Comment = card.addComment(user_id, text, parent_comment_id)

    # Return the created comment
    data = comment.toJson()
    return jsonify(data)

