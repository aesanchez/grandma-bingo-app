from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
#random set of characters
app.config['SECRET_KEY'] = 'dd20c1a3f6b01ec543a0f3ac533460a1'
#db
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
#instancia
db = SQLAlchemy(app)

from app import routes