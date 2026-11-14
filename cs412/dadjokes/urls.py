# David Chung, dwjchung@bu.edu
from django.urls import path

from .views import *

urlpatterns = [
    # url patterns for all the necessary pages
    path('', JokeDetailView.as_view(), name = "jokedetail.html"),
    path('random', JokeDetailView.as_view(), name = "jokedetail.html"),
    path('jokes', AllJokeView.as_view(), name = "alljokes.html"),
    path('joke/<int:pk>', SingleJokeView.as_view(), name = "jokepk.html"),
    path('pictures', AllPictureView.as_view(), name = "allpictures.html"),
    path('picture/<int:pk>', SinglePictureView.as_view(), name = "picturepk.html"),

    # corresponding api urls
    path(r'api/', RandomJokeAPIView.as_view()),
    path(r'api/random', RandomJokeAPIView.as_view()),
    path(r'api/jokes', JokeListAPIView.as_view()),
    path(r'api/joke/<int:pk>', JokeDetailAPIView.as_view()),
    path(r'api/pictures', PictureListAPIView.as_view()),
    path(r'api/picture/<int:pk>', PictureDetailAPIView.as_view()),
    path(r'api/random_picture', RandomPictureAPIView.as_view()),
]