from app import db              #import var db dari dalam app/__init__.py
from datetime import datetime

from app.routes import index   #nah kalai gini baru import library

class User(db.Model):   # membuat tabel user di database dengan format di bawah ini
  id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
  name = db.Column(db.String(250), nullable=False)
  email = db.Column(db.String(100), index=True, nullable=False)
  password = db.Column(db.String(250), nullable=False)
  created_at = db.Column(db.DateTime, default=datetime.utcnow)
  update_at = db.Column(db.DateTime, default=datetime.utcnow)
  
  def __repr__(self):
      return '<User {}>'.format(self.name) # return ke User {Andreas} misalnya
  

