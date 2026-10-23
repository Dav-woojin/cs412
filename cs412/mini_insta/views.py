#David Chung, dwjchung@bu.edu
#this is the views.py file,
#here we create classes for our models and their appropriate templates and context variables

from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from .models import Profile, Post, Photo, Follow, Like
from .forms import CreatePostForm, UpdateProfileForm, UpdatePostForm, CreateProfileForm
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login


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

    def get_object(self):
        if 'pk' in self.kwargs:
            return super().get_object()
        else:
            user = self.request.user
            return Profile.objects.filter(user = user).first()


class PostDetailView(DetailView):
    # PostDetailView is created for showing one post at a time in detail
    model = Post
    template_name = "mini_insta/show_post.html"
    context_object_name = "post"

class CreatePostView(LoginRequiredMixin, CreateView):
    # this is our main class for creating posts, associated with post form
    form_class = CreatePostForm
    template_name = "mini_insta/create_post_form.html"

    def get_object(self):
        user = self.request.user
        return Profile.objects.filter(user = user).first()

    def get_context_data(self):
        # function to get the right context data, based off which profile this post is being made for
        context = super().get_context_data()

        # pk = self.kwargs["pk"]
        # profile = Profile.objects.get(pk=pk)

        context['profile'] = self.get_object()
        return context
    
    
    def form_valid(self, form):
        # form valid function created to appropriately collect the data of the form submission as well as create photo objects from the form
        # pk = self.kwargs["pk"]
        # profile = Profile.objects.get(pk=pk)
        profile = self.get_object()
        form.instance.profile = profile

        response = super().form_valid(form)

        # photourl = self.request.POST["image_url"]
        # Photo.objects.create(post = self.object, image_url = photourl)
        files = self.request.FILES.getlist('files')  
        for file in files:
            Photo.objects.create(post = self.object, image_file = file)

        return response
    
class UpdateProfileView(LoginRequiredMixin, UpdateView):
    # This class manages the update profile functionality, giving the appropriate model, formclass and template
    model = Profile
    form_class = UpdateProfileForm
    template_name = 'mini_insta/update_profile_form.html'

    def get_object(self):
        user = self.request.user
        return Profile.objects.filter(user = user).first()
    
    def get_login_url(self) -> str:
        '''return the URL required for login'''
        return reverse('login')
    
class DeletePostView(LoginRequiredMixin, DeleteView):
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
    
class UpdatePostView(LoginRequiredMixin, UpdateView):
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

class ShowFeedView(LoginRequiredMixin, DetailView):
    # This short class just determines the context object name and which template to go to for showing a feed
    model = Profile
    template_name = "mini_insta/show_feed.html"

    def get_object(self):
        user = self.request.user
        return Profile.objects.filter(user = user).first()

class SearchView(LoginRequiredMixin, ListView):
    # a searchview class meant to provide a search and return the results of filtering post and profile objects with the search query
    template_name = 'mini_insta/search_results.html'

    def get_object(self):
        # we override the normal get_object with a version that links the currently logged in user to the correct profile
        user = self.request.user
        return Profile.objects.filter(user = user).first()
    
    def dispatch(self, request, *args, **kwargs):
        # dispatch function meant to serve the template and request depending on whether we get the specified query from the get request
        template = 'mini_insta/search.html'
        # pk = self.kwargs["pk"]
        # profile = Profile.objects.get(pk = pk)
        # context = {"profile": profile}

        if "query" in self.request.GET:
            return super().dispatch(request, *args, **kwargs)
        else:
            return render(request, template)
        
    def get_queryset(self):
        # a method to grab all the appropriate objects based on the query
        res = Post.objects.filter(caption__contains = self.request.GET["query"])
        return res

    def get_context_data(self, **kwargs: Any):
        # get context data function to grab the right variables for posts and profiles that match our search query
        context = super().get_context_data(**kwargs)

        # pk = self.kwargs["pk"]
        # profile = Profile.objects.get(pk = pk)
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
    
class CreateProfileView(CreateView):
    # a view made for creating profiles, linked to the createprofileform form class
    template_name = "mini_insta/create_profile_form.html"
    form_class = CreateProfileForm
    model = User

    def get_context_data(self, **kwargs):
        # get context data function so that we can initialize a usercreationform
        context = super().get_context_data(**kwargs)
        formU = UserCreationForm()
        context['formU'] = formU
        return context
    
    def form_valid(self, form):
        # formvalid function to 'log' our new user into our database!
        newUser = UserCreationForm(self.request.POST)
        user = newUser.save()
        login(self.request, user, backend='django.contrib.auth.backends.ModelBackend')
        form.instance.user = user
        return super().form_valid(form)
    
class FollowSelect(LoginRequiredMixin, TemplateView):
    # simple templateview class to implement follow functionality
    def dispatch(self, request, *args, **kwargs):
        # this function takes our profile and the profile we are looking at, and creates a follow object between the two
        template = "mini_insta/show_profile.html"

        if self.request.user.is_authenticated:
            ourUser = self.request.user
            ourProfile = Profile.objects.filter(user = ourUser).first()

            otherpk = self.kwargs["pk"]
            otherProfile = Profile.objects.get(pk = otherpk)
            context = {"profile": otherProfile}

            if ourProfile != otherProfile:
                if not Follow.objects.filter(profile = otherProfile,  follower_profile = ourProfile).exists():
                    res = Follow(profile = otherProfile, follower_profile = ourProfile)
                    newfollow = res.save()

        return render(request, template, context)
    
class FollowDelete(LoginRequiredMixin, TemplateView):
    # correspondingly, a delete follow class
    def dispatch(self, request, *args, **kwargs):
        # function to grab the correct profiles and delete the follow object between them
        template = "mini_insta/show_profile.html"

        if self.request.user.is_authenticated:
            ourUser = self.request.user
            ourProfile = Profile.objects.filter(user = ourUser).first()

            otherpk = self.kwargs["pk"]
            otherProfile = Profile.objects.get(pk = otherpk)
            context = {"profile": otherProfile}

            Follow.objects.filter(profile = otherProfile, follower_profile = ourProfile).delete()


        return render(request, template, context)
    
class LikeSelect(LoginRequiredMixin, TemplateView):
    # similar to our followselect, but for likes, allows profiles to like a post
    def dispatch(self, request, *args, **kwargs):
        # function dedicated to creating a like object betewen a profile and a post, checks that it is not the profile's post and that the post has not already been liked by this profile
        template = "mini_insta/show_post.html"

        if self.request.user.is_authenticated:
            ourUser = self.request.user
            ourProfile = Profile.objects.filter(user = ourUser).first()

            post = Post.objects.get(pk = self.kwargs["pk"])
            otherProfile = post.profile
            context = {"post": post}

            if ourProfile != otherProfile:
                if not Like.objects.filter(post = post, profile = ourProfile).exists():
                    res = Like(post = post, profile = ourProfile)
                    newlike = res.save()

        return render(request, template, context)
    
class LikeDelete(LoginRequiredMixin, TemplateView):
    # class dedicated to deleting the appropriate like object
    def dispatch(self, request, *args, **kwargs):
        # grabs the profile that liked the current post, and deletes the likes instance.
        template = "mini_insta/show_post.html"

        if self.request.user.is_authenticated:
            ourUser = self.request.user
            ourProfile = Profile.objects.filter(user = ourUser).first()

            post = Post.objects.get(pk = self.kwargs["pk"])
            otherProfile = post.profile
            context = {"post": post}

            Like.objects.filter(post = post, profile = ourProfile).delete()


        return render(request, template, context)