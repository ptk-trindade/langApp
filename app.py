from flask import Flask, jsonify, request
import json

from auth.routes import auth_bp
from card.routes import card_bp
from feedback.routes import feedback_bp


app = Flask(__name__)

# Register blueprints
app.register_blueprint(auth_bp)
app.register_blueprint(card_bp)
app.register_blueprint(feedback_bp)




if __name__ == '__main__':
    app.run()
