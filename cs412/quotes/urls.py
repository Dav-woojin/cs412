#David Chung, dwjchung@bu.edu
#These are the urlpatterns that we will need to run our quotes app

from django.urls import path
from django.conf import settings
from . import views
 
 
urlpatterns = [ 
    path(r'', views.quote, name="main_page"),
    path(r'quote', views.quote, name="quote_page"),
    path(r'show_all', views.show_all, name="show_all_page"),
    path(r'about', views.about, name="about_page"),
]