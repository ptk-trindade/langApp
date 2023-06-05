from flask import jsonify, request, Blueprint



card_bp = Blueprint('card', __name__)

@card_bp.route('/card/<card_id>/comment', methods=['GET'])
def getComments(card_id: int):
    
    # TODO: Get comments

    # Return the comments
    data = []
    return jsonify(data)


@card_bp.route('/card/comment', methods=['POST'])
def postAddComment():
    # TODO: Validate json (user_id, text, parent_comment_id)

    # TODO: Authenticate the User (by JWT)

    # Return the created comment
    data = []
    return jsonify(data)

