from flask import Flask
from flask_migrate import Migrate
from flask_cors import CORS
from flask_restful import Resource, Api, reqparse, abort


from models import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

CORS(app)
migrate = Migrate(app, db)

db.init_app(app)


if __name__ == '__main__':
    app.run(port=5555)