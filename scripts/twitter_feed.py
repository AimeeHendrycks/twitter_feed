#!/usr/bin/env python

#system tools
import os, sys

#api tools
import requests, base64, json, pprint

#handy
from unidecode import unidecode


CONSUMER_KEY = 'xwQvYHw0vsjBPGBP26kq4QdaQ' 
CONSUMER_SECRET = 'cpPZNGA5lFHTT7eu1qf0GaN5miwMCKjcpI6VxGE1NN4rJmpZCh'

#the base twitter url for sending api requests
URL = 'https://api.twitter.com/oauth2/token'



sys.path.append('..')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 
                    'project.settings')
from main.models import Tweet

#the search term to be used
#SEARCH_TERM = Tweet.search_term

#base64 encode credentials
credentials = base64.urlsafe_b64encode('%s:%s' % (
                    CONSUMER_KEY, CONSUMER_SECRET))

#custom headers for the api keys
custom_headers = {
            'Authorization': 'Basic %s'% (credentials),
            'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
}
#post variable declaring the type of authentication or 'grant type' being used
grant_type_data = 'grant_type=client_credentials'

#putting it all together
#sending a post request to the base twitter URL with the custom headers and post variable
#GET gets params, POST posts data
response = requests.post(URL, headers=custom_headers, data=grant_type_data)

#dump token to variable
access_token = response.json().get('access_token')

#new custom headers that passes access token to twitter
search_headers = {'Authorization': 'Bearer %s' % (access_token)}

#send the request
# param_dict={'q': SEARCH_TERM,'count': 100}
# response = requests.get('https://api.twitter.com/1.1/search/tweets.json', params=param_dict, headers=search_headers)

pp = pprint.PrettyPrinter(indent=2)

#print response.json().get('statuses')[0].keys()
#print response.json().get('statuses')[0]['text']
#print response.json().get('statuses')[0]['user']

#pp.pprint(response.json().get('statuses')[1]['user'])

#from statuses   text, user

#from statuses__user    profile_image_url, screen_name, 
#created_at, time_zone, location

# tweet_list = response.json().get('statuses')
def populate_tweets(search_term):
    print 'populating'
    print search_term
    SEARCH_TERM = search_term
    param_dict={'q': SEARCH_TERM,'count': 100}
    response = requests.get('https://api.twitter.com/1.1/search/tweets.json', params=param_dict, headers=search_headers)
    
    tweet_list = response.json().get('statuses')

    pp.pprint(tweet_list[0]['user'].keys())
    for tweet in tweet_list:
        pp.pprint(tweet.get('text'))
        tweet_location = tweet.get('user').get('location')
        
        if tweet_location != None and tweet_location != '':
            if tweet.get('text') != None:
                new_tweet, created = Tweet.objects.get_or_create(text = str(unidecode(tweet.get('text'))))
                if tweet.get('user').get('profile_image_url') != None:
                    new_tweet.profile_image_url = str(unidecode(tweet.get('user').get('profile_image_url')))
                if tweet.get('user').get('screen_name') != None:
                    new_tweet.screen_name = str(unidecode(tweet.get('user').get('screen_name'))) 
                new_tweet.created_at = tweet.get('created_at').replace('+0000 ', '')
                new_tweet.location =  str(unidecode(tweet_location))
                new_tweet.search_term = SEARCH_TERM

                new_tweet.save()
                print new_tweet
                print ''
        print search_term
    return Tweet.objects.all()
