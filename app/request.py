import urllib.request,json
from .models import Quote

#Getting apikey
apiKey = None

def configure_request(app):
  global base_url
  base_url = app.config['QUOTES_API_BASE_URL']

def get_quote():
  '''
  Function that get the json response to our url request
  '''
  get_quote_url = base_url.format