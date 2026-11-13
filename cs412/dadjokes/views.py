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
    template_name = "dadjokes/jokedetail.html"
    model = Joke
    context_object_name = "joke"

    def get_object(self):
        print("RANDOM CHOICE", random.randint(1, len(Joke.objects.all())))
        i = random.randint(1, len(Joke.objects.all()))
        joke = Joke.objects.get(pk = i)
        self.pic = Picture.objects.get(pk = i)
        return joke

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["pic"] = self.pic
        return context

class AllJokeView(ListView):
    model = Joke
    template_name = "dadjokes/alljokes.html"
    context_object_name = "jokes"

class SingleJokeView(DetailView):
    model = Joke
    template_name = "dadjokes/jokepk.html"
    context_object_name = "joke"

    def get_context_data(self, **kwargs):
        # function to get the right context data, based off which profile this post is being made for
        context = super().get_context_data(**kwargs)

        pk = self.kwargs["pk"]
        joke = Joke.objects.get(pk=pk)

        context['joke'] = joke
        return context

class AllPictureView(ListView):
    model = Picture
    template_name = "dadjokes/allpictures.html"
    context_object_name = "pictures"

class SinglePictureView(DetailView):
    model = Picture
    template_name = "dadjokes/picturepk.html"
    context_object_name = "pictures"

    def get_context_data(self, **kwargs):
        # function to get the right context data, based off which profile this post is being made for
        context = super().get_context_data(**kwargs)

        pk = self.kwargs["pk"]
        picture = Picture.objects.get(pk=pk)

        context['picture'] = picture
        return context

class RandomJokeAPIView(generics.RetrieveAPIView):
    # looked up documentation for a better single model view
    queryset = Joke.objects.all()
    serializer_class = JokeSerializer

    def get_object(self):
        i = random.randint(1, len(Joke.objects.all()))
        joke = Joke.objects.get(pk = i)
        return joke

class RandomPictureAPIView(generics.RetrieveAPIView):
    queryset = Picture.objects.all()
    serializer_class = PictureSerializer

    def get_object(self):
        i = random.randint(1, len(Joke.objects.all()))
        pic = Picture.objects.get(pk = i)
        return pic

class JokeListAPIView(generics.ListCreateAPIView):
    queryset = Joke.objects.all()
    serializer_class = JokeSerializer
 
class JokeDetailAPIView(generics.RetrieveAPIView):
    queryset = Joke.objects.all()
    serializer_class = JokeSerializer

    def get_context_data(self, **kwargs):
        # function to get the right context data, based off which profile this post is being made for
        context = super().get_context_data(**kwargs)

        pk = self.kwargs["pk"]
        joke = Joke.objects.get(pk=pk)

        context['joke'] = joke
        return context

class PictureListAPIView(generics.ListCreateAPIView):
    queryset = Picture.objects.all()
    serializer_class = PictureSerializer
 
class PictureDetailAPIView(generics.RetrieveAPIView):
    queryset = Picture.objects.all()
    serializer_class = PictureSerializer

    def get_context_data(self, **kwargs):
        # function to get the right context data, based off which profile this post is being made for
        context = super().get_context_data(**kwargs)

        pk = self.kwargs["pk"]
        pic = Picture.objects.get(pk=pk)

        context['pic'] = pic
        return context