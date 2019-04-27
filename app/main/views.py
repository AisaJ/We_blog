from . import main
from flask import render_template,request,redirect,url_for,abort,flash
from ..request import get_quote

@main.route('/')
def index():
  random_quote = get_quote()  

  return render_template('index.html',quote=random_quote)