#David Chung, dwjchung@bu.edu
#this is the views.py file,
#here we create classes for our models and their appropriate templates and context variables

from typing import Any
from django.db.models.query import QuerySet
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
    # This class manages the update profile functionality, giving the appropriate model, formclass and template
    model = Profile
    form_class = UpdateProfileForm
    template_name = 'mini_insta/update_profile_form.html'
    
class DeletePostView(DeleteView):
    # This class manages the delete post functionality, giving the appropriate model, formclass and template
    model = Post
    template_name = "mini_insta/delete_post_form.html"

    def get_context_data(self, **kwargs):
        # We give back the profile and post data as context for a given post deletion
        context = super().get_context_data(**kwargs)

        pk = self.kwargs["pk"]
        post = self.object

        context['profile'] = post.profile
        context['post'] = post
        return context
    
    def get_success_url(self):
        # this handles how the app should behave upon successful post deletion
        pk = self.kwargs["pk"]
        post = Post.objects.get(pk=pk)
        profile = post.profile
        return reverse('show_profile', kwargs={'pk': profile.pk })
    
class UpdatePostView(UpdateView):
    # this is the view to handle updating a post, with the appropriate model, formclass, and template name provided
    model = Post
    form_class = UpdatePostForm
    template_name = "mini_insta/update_post_form.html"

    def get_context_data(self, **kwargs):
        # this method takes our current post object and gives the appropriate profile and post context
        context = super().get_context_data(**kwargs)

        post = self.object

        context['profile'] = post.profile
        context['post'] = post
        return context
    
    def get_success_url(self):
        # this method handles where the application should go after successfully updating a post
        pk = self.kwargs["pk"]
        post = Post.objects.get(pk=pk)
        return reverse('show_post', kwargs={'pk': post.pk })

class ShowFollowersDetailView(DetailView):
    # This short class just determines the context object name and which template to go to for showing followers
    model = Profile
    context_object_name = "profile"
    template_name = "mini_insta/show_followers.html"

class ShowFollowingDetailView(DetailView):
    # This short class just determines the context object name and which template to go to for showing followings
    model = Profile
    context_object_name = "profile"
    template_name = "mini_insta/show_following.html"

class ShowFeedView(DetailView):
    # This short class just determines the context object name and which template to go to for showing a feed
    model = Profile
    template_name = "mini_insta/show_feed.html"

class SearchView(ListView):
    template_name = 'mini_insta/search_results.html'
    
    def dispatch(self, request, *args, **kwargs):
        template = 'mini_insta/search.html'
        pk = self.kwargs["pk"]
        profile = Profile.objects.get(pk = pk)
        context = {"profile": profile}

        if "query" in self.request.GET:
            return super().dispatch(request, *args, **kwargs)
        else:
            return render(request, template, context)
        
    def get_queryset(self):
        res = Post.objects.filter(caption__contains = self.request.GET["query"])
        return res

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)

        pk = self.kwargs["pk"]
        profile = Profile.objects.get(pk = pk)
        if "query" in self.request.GET:
            query = self.request.GET["query"]
            context['query'] = query
        context['posts'] = self.get_queryset()

        profiles = set()
        for p in Profile.objects.filter(username__contains = self.request.GET["query"]):
            profiles.add(p)
        for p in Profile.objects.filter(display_name__contains = self.request.GET["query"]):
            profiles.add(p)
        for p in Profile.objects.filter(bio_text__contains = self.request.GET["query"]):
            profiles.add(p)
        profile_list = list(profiles)
        context['profiles'] = profile_list

        return context