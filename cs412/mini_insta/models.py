#David Chung, dwjchung@bu.edu
#In this models file, we create our Profile class that holds all the apropriate info
#for each user, as well as defining an appropriate to string method for readability in admin
# in assignment 4, we also added post and photo models for appropriate usage in forms and in our database

from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)

    username = models.TextField(blank = True)
    display_name = models.TextField(blank = True)
    profile_image_url = models.URLField(blank = True)
    bio_text = models.TextField(blank = True)
    join_date = models.DateTimeField(auto_now = True)

    def __str__(self):
        #tostring method for profile
        return f'{self.username}'
    
    def get_all_posts(self):
        #get all posts method for profile, this is used in order to display all the posts associated with a certain user
        posts = Post.objects.filter(profile = self).order_by('timestamp')
        return posts
    
    def get_absolute_url(self):
        return reverse("show_profile", kwargs = {'pk': self.pk})
    
    def get_followers(self):
        return Follow.objects.filter(profile = self)
    
    def get_num_followers(self):
        return len(Follow.objects.filter(profile = self))
    
    def get_following(self):
        return Follow.objects.filter(follower_profile = self)
    
    def get_num_following(self):
        return len(Follow.objects.filter(follower_profile = self))
    
    def get_post_feed(self):
        combined_result = Post.objects.none()
        following_profiles = Follow.objects.filter(follower_profile = self)
        for p in following_profiles:
            combined_result = combined_result | Post.objects.filter(profile = p.profile)

        return combined_result

    
class Post(models.Model):
    profile = models.ForeignKey(Profile, on_delete = models.CASCADE)
    timestamp = models.DateTimeField(auto_now = True)
    caption = models.TextField(blank = True)

    def __str__(self):
        #tostring method for post
        return f'{self.caption} for profile: {self.profile}'
    
    def get_all_photos(self):
        #get all photos method for post, used to access all photos associated with a post
        photos = Photo.objects.filter(post = self)
        return photos
    
    def get_first_photo(self):
        #get first photo method for easy usage when we need a display photo in a profile
        photos = Photo.objects.filter(post = self)
        if photos:
            photo = photos[0]
            return photo
        else:
            return None
        
    def get_absolute_url(self):
        #provides a return url after we finish a post form submission
        return reverse('show_post', kwargs={'pk': self.pk})
    
    def get_all_comments(self):
        return Comment.objects.filter(post = self)
    
    def get_likes(self):
        return Like.objects.filter(post = self)
    
    def get_like_count(self):
        return len(Like.objects.filter(post = self))
    
class Photo(models.Model):
    post = models.ForeignKey(Post, on_delete = models.CASCADE)
    image_url = models.URLField(blank = True)
    timestamp = models.DateTimeField(auto_now = True)
    image_file = models.ImageField(blank = True)

    def __str__(self):
        #tostring for photo
        return f'{self.image_file} for post: {self.post}'
    
    def get_image_url(self):
        #gives back the correct url depending on if we have an image file or an actual url and none in case of a failure
        if self.image_file:
            return self.image_file.url
        if self.image_url:
            return self.image_url
        return None
    
class Follow(models.Model):
    profile = models.ForeignKey(Profile, related_name="profile", on_delete = models.CASCADE)
    follower_profile = models.ForeignKey(Profile, related_name="follower_profile", on_delete = models.CASCADE)
    timestamp = models.DateTimeField(auto_now = True)

    def __str__(self):
        return f'{self.follower_profile} follows {self.profile}'
    
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete = models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete = models.CASCADE)
    timestamp = models.DateTimeField(auto_now = True)
    text = models.TextField(blank = True)

    def __str__(self):
        return f'{self.text}'
    

class Like(models.Model):
    post = models.ForeignKey(Post, on_delete = models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete = models.CASCADE)
    timestamp = models.DateTimeField(auto_now = True)

    def __str__(self):
        return f'{self.profile} likes {self.post}'
    
    