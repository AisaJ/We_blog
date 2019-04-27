from . import db
from datetime import datetime

class Quote:
  '''
  class to define quote objects
  '''
  def __init__(self,id,author,quote):
    self.id = id
    self.author = author
    self.quote = quote

class Blog(db.Model):
  '''
  Class that defines blog objects
  '''
  __tablename__ = 'blogs'

  id = db.Column(db.Integer,primary_key=True)
  title = db.Column(db.String(255))
  blog = db.Column(db.String(255))
  category = db.Column(db.String(255))
  added_date = db.Column(db.DateTime,default=datetime.utcnow)
  blogger = db.Column(db.Integer,db.ForeignKey('users.id'))  

  def __repr__(self):
    return f'Blog{self.blog}'

class User(UserMixin,db.Model):
  '''
  Defining users objects
  '''
  __tablename__ = 'users'
  id = db.Column(db.Integer,primary_key = True)
  username =  db.Column(db.String(255),index = True)
  email =  db.Column(db.String(255),unique = True,index=True)
  bio = db.Column(db.String(255))
  profile_pic_path  = db.Column(db.String())
  password_secure = db.Column(db.String(255))
  blogs =  db.relationship('Blog',backref = 'user',lazy='dynamic')
  @property
  def password(self):
    raise AttributeError('You cannot read the password attribute')

  @password.setter
  def password(self,password):
    self.password_secure = generate_password_hash(password)

  def verify_password(self,password):
    return check_password_hash(self.password_secure,password)

  def __repr__(self):
    return f'User {self.username}'

