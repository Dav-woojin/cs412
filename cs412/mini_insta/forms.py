# David Chung, dwjchung@bu.edu
# This is our forms.py file where I define the class for creating a post form based on the model form from models

from django import forms
from .models import *

class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['caption']

class UpdateProfileForm(forms.ModelForm): 
    class Meta: 
        model = Profile
        fields = ['display_name', 'profile_image_url', 'bio_text']

class UpdatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['caption']

class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['username', 'display_name', 'bio_text', 'profile_image_url']