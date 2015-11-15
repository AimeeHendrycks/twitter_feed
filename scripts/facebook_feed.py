#!/usr/bin/env python

#system tools
import os, sys

#api tools
import requests, base64, json, pprint

#handy
from unidecode import unidecode

CONSUMER_KEY = '1519072575080235'
CONSUMER_SECRET = '3d350157c4d8e995dc773fd47f8f07f1'


sys.path.append('..')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 
                    'project.settings')
URL = 'https://graph.facebook.com/oauth/access_token?'
  client_id={'1519072575080235'}&
  client_secret={'3d350157c4d8e995dc773fd47f8f07f1'}&
  grant_type=fb_exchange_token
  
1519072575080235|1Zgu9UfnoLRvzb73TA9KrNHXClc

SEARCH_TERM = 'cats'

credentials = base64.urlsafe_b64encode('%s:%s' % (CONSUMER_KEY, CONSUMER_SECRET))

custom_headers = {  
                    'Authorization': 'Basic %s' % (credentials),
                    'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
                 }
grant_type_data = 'grant_type=client_credentials'

response = requests.post(URL, headers=custom_headers, data=grant_type_data)
print response.json()
