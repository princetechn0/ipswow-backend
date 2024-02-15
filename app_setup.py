from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import os

app = Flask(__name__, static_folder="../frontend/build")
CORS(app)
DATABASE_URL = os.environ['DATABASE_URL']
index = DATABASE_URL.find("postgres")
modified_url = DATABASE_URL[:index + len("postgres")] + "ql" + DATABASE_URL[index + len("postgres"):]

app.config['SQLALCHEMY_DATABASE_URI'] = modified_url

db = SQLAlchemy(app)
