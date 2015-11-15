#!/usr/bin/env python
import requests, pprint
import sys
import os
from unidecode import unidecode

sys.path.append('..')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'project.settings')

import django
from django.conf import settings
from main.models import Instagram_post
def populate_posts(search_term):
    print 'populating'
    SEARCH_TERM=search_term
    param_dict = {'access_token': '2245465432.1fb234f.4edc0a9c01e44ac2820f03ceeebaea19', 'callback':'?', 'count':100}
    response = requests.get('https://api.instagram.com/v1/tags/%s/media/recent'% SEARCH_TERM, params=param_dict)
    post_list = response.json().get('data')
    if len(post_list) != 0:
        for post in post_list:
            location = post.get('location')
            if post.get('caption').get('text') != '':      
                new_post, created = Instagram_post.objects.get_or_create(text= str(unidecode(post.get('caption').get('text'))))
                print new_post.text
                new_post.username = post.get('caption').get('from').get('username')
                new_post.profile_picture = post.get('caption').get('from').get('profile_picture')
                new_post.location = location
                new_post.link = post.get('link')
                new_post.post_image = post.get('images').get('standard_resolution').get('url')
                new_post.search_term = SEARCH_TERM
                new_post.save()
        return Instagram_post.objects.all()

