from django.contrib import admin
from main.models import Tweet, Instagram_post
# Register your models here.
class TweetAdmin(admin.ModelAdmin):
    list_display = ('text', 'screen_name')
    search_fields = ['text']

class InstagramPostAdmin(admin.ModelAdmin):
    list_display = ('text', 'username')
    search_fields = ['text']

admin.site.register(Tweet, TweetAdmin)
admin.site.register(Instagram_post, InstagramPostAdmin)