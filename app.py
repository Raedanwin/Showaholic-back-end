from flask import Flask, jsonify, g
from flask_cors import CORS
from flask_login import LoginManager

import models

login_manager = LoginManager()

DEBUG = True
PORT = 8000

# from resources.users import user

app = Flask(__name__)

app.secret_key = 'thisisasecret'
login_manager.init_app(app)

# @login_manager.user_loader
# def load_user(userid):
#     try:
#         return models.User.get(models.User.id == userid)
#     except models.DoesNotExist:
#         return None

# @app.before_request
# def before_request():
#     g.db models.DATABASE
#     g.db.connect()

# @app.after_request
# def after_request(response):
#     g.db.close()
#     return response

# CORS(user, origins = '*', supports_credentials = True)

# app.register_blueprint(user, user_prefix = '/user')

@app.route('/')
def index():
    return 'hi'

if __name__ == '__main__':
    app.run(debug = DEBUG, port = PORT)