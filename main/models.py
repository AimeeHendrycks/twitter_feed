from django.db import models

# Create your models here.
class Tweet(models.Model):
    text = models.CharField(max_length=255, null=True, blank=True)
    profile_image_url = models.CharField(max_length=255, null=True, blank=True)
    screen_name = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.CharField(max_length=255, null=True, blank=True)
    location = models.CharField(max_length=255, null=True, blank=True)
    search_term = models.CharField(max_length=255, null=True, blank=True)
    
    def __unicode__(self):
        return self.text

class Instagram_post(models.Model):
    text = models.CharField(max_length=255, null=True, blank=True)
    username = models.CharField(max_length=255, null=True, blank=True)
    profile_picture = models.CharField(max_length=255, null=True, blank=True)
    text = models.CharField(max_length=255, null=True, blank=True)
    location = models.CharField(max_length=255, null=True, blank=True)
    link = models.CharField(max_length=255, null=True, blank=True)
    post_image = models.CharField(max_length=255, null=True, blank=True)
    search_term = models.CharField(max_length=255, null=True, blank=True)

    def __unicode__(self):
        return self.text