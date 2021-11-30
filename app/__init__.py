from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)           # Default
app.config.from_object(Config)  # 
db = SQLAlchemy(app)            # var db isinya SQLAlchemy (dari app/__init__.py)
migrate = Migrate(app, db)      # var migrate untuk migrate, di dalam () itu formatnya untuk mengoneksikan antara app dan db

from app.model import user, dosen, mahasiswa
from app import routes

