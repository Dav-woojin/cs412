#David Chung, dwjchung@bu.edu
#this is the views.py file,
#here we create classes for our models and their appropriate templates and context variables

from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Profile, Post, Photo
from .forms import CreatePostForm
from django.urls import reverse

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

class PostDetailView(DetailView):
    model = Post
    template_name = "mini_insta/show_post.html"
    context_object_name = "post"

class CreatePostView(CreateView):
    form_class = CreatePostForm
    template_name = "mini_insta/create_post_form.html"

    def get_context_data(self):
        context = super().get_context_data()

        pk = self.kwargs["pk"]
        profile = Profile.objects.get(pk=pk)

        context['profile'] = profile
        return context
    
    # def get_success_url(self):
    #     pk = self.kwargs["pk"]
    #     return reverse('show_post', kwargs={'pk': pk })
    
    def form_valid(self, form):
        pk = self.kwargs["pk"]
        profile = Profile.objects.get(pk=pk)
        form.instance.profile = profile

        response = super().form_valid(form)

        photourl = self.request.POST["image_url"]
        Photo.objects.create(post = self.object, image_url = photourl)


        return response