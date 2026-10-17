#David Chung, dwjchung@bu.edu
#this is the views.py file,
#here we create classes for our models and their appropriate templates and context variables

from typing import Any
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Profile, Post, Photo
from .forms import CreatePostForm, UpdateProfileForm, UpdatePostForm
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
    # PostDetailView is created for showing one post at a time in detail
    model = Post
    template_name = "mini_insta/show_post.html"
    context_object_name = "post"

class CreatePostView(CreateView):
    # this is our main class for creating posts, associated with post form
    form_class = CreatePostForm
    template_name = "mini_insta/create_post_form.html"

    def get_context_data(self):
        # function to get the right context data, based off which profile this post is being made for
        context = super().get_context_data()

        pk = self.kwargs["pk"]
        profile = Profile.objects.get(pk=pk)

        context['profile'] = profile
        return context
    
    
    def form_valid(self, form):
        # form valid function created to appropriately collect the data of the form submission as well as create photo objects from the form
        pk = self.kwargs["pk"]
        profile = Profile.objects.get(pk=pk)
        form.instance.profile = profile

        response = super().form_valid(form)

        # photourl = self.request.POST["image_url"]
        # Photo.objects.create(post = self.object, image_url = photourl)
        files = self.request.FILES.getlist('files')  
        for file in files:
            Photo.objects.create(post = self.object, image_file = file)

        return response
    
class UpdateProfileView(UpdateView):
    model = Profile
    form_class = UpdateProfileForm
    template_name = 'mini_insta/update_profile_form.html'
    
class DeletePostView(DeleteView):
    model = Post
    template_name = "mini_insta/delete_post_form.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        pk = self.kwargs["pk"]
        post = self.object

        context['profile'] = post.profile
        context['post'] = post
        return context
    
    def get_success_url(self):
        pk = self.kwargs["pk"]
        post = Post.objects.get(pk=pk)
        profile = post.profile
        return reverse('show_profile', kwargs={'pk': profile.pk })
    
class UpdatePostView(UpdateView):
    model = Post
    form_class = UpdatePostForm
    template_name = "mini_insta/update_post_form.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        pk = self.kwargs["pk"]
        post = self.object

        context['profile'] = post.profile
        context['post'] = post
        return context
    
    def get_success_url(self):
        pk = self.kwargs["pk"]
        post = Post.objects.get(pk=pk)
        return reverse('show_post', kwargs={'pk': post.pk })

