from django.shortcuts import render, render_to_response
from django.template import RequestContext
from main.models import Tweet, Instagram_post
from django.views.generic.list import ListView
from scripts.twitter_feed import populate_tweets
from scripts.instagram_feed import populate_posts

# Create your views here.

def base(request):
    context = {}
    return render_to_response('base.html', context, context_instance=RequestContext(request))

def home(request):
    context = {}
    return render_to_response('home.html', context, RequestContext(request))

class TweetListView(ListView):
    model = Tweet
    template_name= 'tweet_list.html'
    object_list = []
    def get_queryset(self):
        object_list = []
        if 'search' in self.request.GET:
            search_term = self.request.GET['search']
            Tweet.objects.all().delete()
            if search_term != '':
                object_list = populate_tweets(search_term)
                print object_list
            else:
                object_list = []
        else:
            pass
        return object_list
    if object_list != None:
        paginate_by= 10

class InstagramPostListView(ListView):
    model = Instagram_post
    template_name= 'instagram_post_list.html' 
    object_list = ''
    def get_queryset(self):
        object_list = ''
        if 'search' in self.request.GET:
            search_term = self.request.GET['search'].replace(' ', '')
            print search_term
            Instagram_post.objects.all().delete()
            if search_term != '' or search_term != None:
                object_list = populate_posts(search_term)
                print object_list
        else:
            pass
        return object_list
    if object_list != None:
        paginate_by= 10   

# def get_context_data(self, **kwargs):
    #         context = super(TweetListView, self).get_context_data(**kwargs)
    #         context['form'] = SearchForm()
    #         return context