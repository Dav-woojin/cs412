from django.urls import path
from django.conf import settings
from . import views
 
#David Chung
#dwjchung@bu.edu
#this is a urls file to determine the urls for each page we want for our app
urlpatterns = [ 
    path(r'main', views.main, name="main"),
    path(r'order', views.order, name="order"),
    path(r'confirmation', views.confirmation, name="confirmation"),
]
 