from flask import jsonify, request, Blueprint

from models import userAuth


card_bp = Blueprint('card', __name__)

@card_bp.route('/card/byUser', methods=['POST'])
def getCardByUser():
    # TODO: Validate json
    
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


@card_bp.route('/card/byConcept', methods=['POST'])
def getCardByConcept():
    # TODO: Validate json
    
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

