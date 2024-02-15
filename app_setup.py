from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__, static_folder="../frontend/build")
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://hmnujahcbcycmg:afb438b294cd8aa20fa7b9924b5ca632330cc7693277f5565b70ba60f7a3d6ec@ec2-34-193-110-25.compute-1.amazonaws.com:5432/d6j9pqtj1paevl'


app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Corrected line

db = SQLAlchemy(app)
