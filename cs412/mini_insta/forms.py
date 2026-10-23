# David Chung, dwjchung@bu.edu
# This is our forms.py file where I define the class for creating a post form based on the model form from models

from django import forms
from .models import *

class CreatePostForm(forms.ModelForm):
    # form for creating a post
    class Meta:
        model = Post
        fields = ['caption']

class UpdateProfileForm(forms.ModelForm): 
    # form for updating a profile
    class Meta: 
        model = Profile
        fields = ['display_name', 'profile_image_url', 'bio_text']

class UpdatePostForm(forms.ModelForm):
    # form for updating a post
    class Meta:
        model = Post
        fields = ['caption']

class CreateProfileForm(forms.ModelForm):
    # form for creating a profile
    class Meta:
        model = Profile
        fields = ['username', 'display_name', 'bio_text', 'profile_image_url']