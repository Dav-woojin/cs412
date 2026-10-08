# David Chung, dwjchung@bu.edu
# This is our forms.py file where I define the class for creating a post form based on the model form from models

from django import forms
from .models import *

class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['caption']