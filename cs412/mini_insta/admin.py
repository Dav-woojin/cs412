#David Chung, dwjchung@bu.edu
#in our admin file, we register our profile model for use in the admin webpage

from django.contrib import admin

# Register your models here.
from .models import Profile, Post, Photo

admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(Photo)
