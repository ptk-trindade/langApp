from flask import Flask, jsonify, request
import json

from user.routes import user_bp
from userAuthentication.routes import auth_bp


app = Flask(__name__)

# Register blueprints
app.register_blueprint(user_bp)
app.register_blueprint(auth_bp)




if __name__ == '__main__':
    app.run()
