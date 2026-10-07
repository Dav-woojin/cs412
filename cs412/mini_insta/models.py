#David Chung, dwjchung@bu.edu
#In this models file, we create our Profile class that holds all the apropriate info
#for each user, as well as defining an appropriate to string method for readability in admin

from django.db import models
from django.urls import reverse

# Create your models here.

class Profile(models.Model):
    username = models.TextField(blank = True)
    display_name = models.TextField(blank = True)
    profile_image_url = models.URLField(blank = True)
    bio_text = models.TextField(blank = True)
    join_date = models.DateTimeField(auto_now = True)

    def __str__(self):
        return f'{self.username}'
    
    
    def get_all_posts(self):
        posts = Post.objects.filter(profile = self).order_by('timestamp')
        return posts
    
    
class Post(models.Model):
    profile = models.ForeignKey(Profile, on_delete = models.CASCADE)
    timestamp = models.DateTimeField(auto_now = True)
    caption = models.TextField(blank = True)

    def __str__(self):
        return f'{self.caption} for profile: {self.profile}'
    
    def get_all_photos(self):
        photos = Photo.objects.filter(post = self)
        return photos
    
    def get_first_photo(self):
        photos = Photo.objects.filter(post = self)
        if photos:
            photo = photos[0]
            return photo
        else:
            return None
        
    def get_absolute_url(self):
        return reverse('show_post', kwargs={'pk': self.pk})
    
class Photo(models.Model):
    post = models.ForeignKey(Post, on_delete = models.CASCADE)
    image_url = models.URLField(blank = True)
    timestamp = models.DateTimeField(auto_now = True)

    def __str__(self):
        return f'{self.image_url} for post: {self.post}'