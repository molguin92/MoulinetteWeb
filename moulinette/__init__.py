import os

from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from itsdangerous import URLSafeSerializer

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
app.config['SECRET_KEY'] = os.environ['SECRET_KEY']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
api = Api(app)
serializer = URLSafeSerializer(app.config['SECRET_KEY'])

from moulinette.homework import models
import moulinette.views

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
