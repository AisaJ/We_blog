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
  

  def __repr__(self):
    return f'Blog{self.blog}'
