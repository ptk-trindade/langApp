from flask import jsonify, request, Blueprint

feedback_bp = Blueprint('feedback', __name__)

@feedback_bp.route('/feedback/difficulty', methods=['POST'])
def getCardByUser():
    # TODO: Validate json
    
    # TODO: Authenticate the User (by JWT)
    bearer = request.headers.get('Authorization')

    # TODO: Do the thing
    
    return jsonify({"success": True, "message": ""})


