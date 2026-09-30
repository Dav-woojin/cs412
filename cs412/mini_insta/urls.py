#David Chung, dwjchung@bu.edu
#This is the urls file, in which we create the paths to the appropriate urls for our
#app, a show all page and individual show profile pages

from django.urls import path
from .views import ProfileListView, ProfileDetailView


urlpatterns = [
    path('', ProfileListView.as_view(), name = "show_all_profiles"),
    path('profile/<int:pk>', ProfileDetailView.as_view(), name = 'show_profile'),
]