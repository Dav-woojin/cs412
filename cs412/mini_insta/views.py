#David Chung, dwjchung@bu.edu
#this is the views.py file,
#here we create classes for our models and their appropriate templates and context variables

from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Profile

# Create your views here.
class ProfileListView(ListView):
    # ProfileListView is dedicated to showing all profiles on the show all page
    model = Profile
    template_name = "mini_insta/show_all_profiles.html"
    context_object_name = "profiles"

class ProfileDetailView(DetailView):
    # ProfileListView is dedicated to showing one profile at a time
    model = Profile
    template_name = "mini_insta/show_profile.html"
    context_object_name = "profile"