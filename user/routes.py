from flask import jsonify, request, Blueprint

from userAuthentication import userAuthentication


user_bp = Blueprint('user', __name__)

@user_bp.route('/user/card', methods=['GET'])
def getCardByUser():
    # TODO: Authenticate the User (by JWT)
    bearer = request.headers.get('Authorization')


    # TODO: Get the card (CardPicking)


    # Return the card
    data = {
        'concepts': [{'id': 1, 'name': 'Chair', 'description': 'Used to sit on', 'type': 'word'}],
        'hasAudio': False,
        'front': 'Chair',
        'back': 'Cadeira',
        'card_id': 123
    }
    
    return jsonify(data)


@user_bp.route('/user/card/<concept_id>', methods=['GET'])
def getCardByConcept(concept_id):
    
    # TODO: Authenticate the User (by JWT)
    bearer = request.headers.get('Authorization')
    auth = userAuthentication.UserAuthentication()
    user_id = auth.authenticateJwt(bearer)



    # TODO: Get the card (CardPicking)


    # Return the card
    data = {
        'concepts': [{'id': 1, 'name': 'Chair', 'description': 'Used to sit on', 'type': 'word'}],
        'hasAudio': False,
        'front': 'Chair',
        'back': 'Cadeira',
        'card_id': 123
    }    
    return jsonify(data)


@user_bp.route('/user/feedback/difficulty', methods=['POST'])
def postFeedback():
    # TODO: Validate json (card_id, difficulty)
    
    # TODO: Authenticate the User (by JWT)
    bearer = request.headers.get('Authorization')

    # TODO: Do the thing
    
    return jsonify({"success": True, "message": ""})