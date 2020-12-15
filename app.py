from flask import Flask, g
from flask_cors import CORS

import models
from resources.watchlist import watchlist

DEBUG = True
PORT = 8000

app = Flask(__name__)

@app.before_request
def before_request():
    """Connect to the database before each request."""
    g.db = models.DATABASE
    g.db.connect()

@app.after_request
def after_request(res):
    """Close the database connection after each request."""
    g.db.close()
    return res

@app.route('/')
def index():
    return 'hi'

CORS(watchlist, origins=['http://localhost:3000'], supports_credentials=True)

app.register_blueprint(watchlist, url_prefix='/api/v1/watchlist')

if __name__ == '__main__':
    models.initialize()
    app.run(debug=DEBUG, port=PORT)
