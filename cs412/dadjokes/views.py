# David Chung, dwjchung@bu.edu
# views file to implement functionality for each main element of app
from django.shortcuts import render

import random
# Create your views here.
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Joke, Picture
from rest_framework import generics
from .serializers import *

class JokeDetailView(DetailView):
    # handles one random choice for a joke and a photo
    template_name = "dadjokes/jokedetail.html"
    model = Joke
    context_object_name = "joke"

    def get_object(self):
        # get object gets a random joke
        print("RANDOM CHOICE", random.randint(1, len(Joke.objects.all())))
        i = random.randint(1, len(Joke.objects.all()))
        joke = Joke.objects.get(pk = i)
        return joke

    def get_context_data(self, **kwargs):
        # this gets a random picture
        context = super().get_context_data(**kwargs)
        i = random.randint(1, len(Joke.objects.all()))
        pic= Picture.objects.get(pk = i)
        context["pic"] = pic
        return context

class AllJokeView(ListView):
    # view for displaying all jokes
    model = Joke
    template_name = "dadjokes/alljokes.html"
    context_object_name = "jokes"

class SingleJokeView(DetailView):
    # view to display a joke based on a certain pk
    model = Joke
    template_name = "dadjokes/jokepk.html"
    context_object_name = "joke"

    def get_context_data(self, **kwargs):
        # get context data to get to appropriate joke object
        context = super().get_context_data(**kwargs)

        pk = self.kwargs["pk"]
        joke = Joke.objects.get(pk=pk)

        context['joke'] = joke
        return context

class AllPictureView(ListView):
    # view to get all pictures
    model = Picture
    template_name = "dadjokes/allpictures.html"
    context_object_name = "pictures"

class SinglePictureView(DetailView):
    # view to get a picture based on pk
    model = Picture
    template_name = "dadjokes/picturepk.html"
    context_object_name = "pictures"

    def get_context_data(self, **kwargs):
        # get context data to get to appropriate joke object based on pk
        context = super().get_context_data(**kwargs)

        pk = self.kwargs["pk"]
        picture = Picture.objects.get(pk=pk)

        context['picture'] = picture
        return context

class RandomJokeAPIView(generics.RetrieveAPIView):
    # looked up documentation for a better single model view, RetrieveAPIView
    # view to get one random joke for api
    queryset = Joke.objects.all()
    serializer_class = JokeSerializer

    def get_object(self):
        # gets random joke
        i = random.randint(1, len(Joke.objects.all()))
        joke = Joke.objects.get(pk = i)
        return joke

class RandomPictureAPIView(generics.RetrieveAPIView):
    # api view to get a random picture
    queryset = Picture.objects.all()
    serializer_class = PictureSerializer

    def get_object(self):
        # get object grabs one random picture
        i = random.randint(1, len(Joke.objects.all()))
        pic = Picture.objects.get(pk = i)
        return pic

class JokeListAPIView(generics.ListCreateAPIView):
    # view to get all jokes
    queryset = Joke.objects.all()
    serializer_class = JokeSerializer
 
class JokeDetailAPIView(generics.RetrieveAPIView):
    # view to one joke by pk
    queryset = Joke.objects.all()
    serializer_class = JokeSerializer

    def get_context_data(self, **kwargs):
        # get context data to assign the right joke object
        context = super().get_context_data(**kwargs)

        pk = self.kwargs["pk"]
        joke = Joke.objects.get(pk=pk)

        context['joke'] = joke
        return context

class PictureListAPIView(generics.ListCreateAPIView):
    # view to get all picture objects
    queryset = Picture.objects.all()
    serializer_class = PictureSerializer
 
class PictureDetailAPIView(generics.RetrieveAPIView):
    # view to get one picture object for api
    queryset = Picture.objects.all()
    serializer_class = PictureSerializer

    def get_context_data(self, **kwargs):
        # get context data for one picture based on pk for api
        context = super().get_context_data(**kwargs)

        pk = self.kwargs["pk"]
        pic = Picture.objects.get(pk=pk)

        context['pic'] = pic
        return context