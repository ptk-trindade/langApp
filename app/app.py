from flask import Flask, jsonify, request
import database.db as db

from cardComment.routes import card_bp
from userCard.routes import user_bp
from userAuthentication.routes import auth_bp


app = Flask(__name__)

# Register blueprints
app.register_blueprint(card_bp)
app.register_blueprint(user_bp)
app.register_blueprint(auth_bp)


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
