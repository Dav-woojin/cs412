#David Chung, dwjchung@bu.edu
#This is the urls file, in which we create the paths to the appropriate urls for our
#app, a show all page and individual show profile pages

from django.urls import path
from .views import *

from django.contrib.auth import views as auth_views

urlpatterns = [
    # all of our early/initial urls
    path('', ProfileListView.as_view(), name = "show_all_profiles"),
    path('profile/<int:pk>', ProfileDetailView.as_view(), name = 'show_profile'),
    path('post/<int:pk>', PostDetailView.as_view(), name = 'show_post'),
    path('post/<int:pk>/delete', DeletePostView.as_view(), name = 'delete'),
    path('post/<int:pk>/update', UpdatePostView.as_view(), name = 'update'),
    path('profile/<int:pk>/followers', ShowFollowersDetailView.as_view(), name = 'followers'),
    path('profile/<int:pk>/following', ShowFollowingDetailView.as_view(), name = 'following'),

    # updated urls, now not using pk!
    path('profile/feed', ShowFeedView.as_view(), name = "show_feed"),
    path('profile/search', SearchView.as_view(), name = "search"),
    path('profile/create_post', CreatePostView.as_view(), name = 'create_post'),
    path('profile/update', UpdateProfileView.as_view(), name = 'update_profile'),

    # new profile url, just for our current user without pk specification
    path('profile', ProfileDetailView.as_view(), name = 'show_profile'),

    # login logout urls
    path('login/', auth_views.LoginView.as_view(template_name = "mini_insta/login.html"), name = "login"),
    path('logout/', auth_views.LogoutView.as_view(next_page='show_all_profiles'), name='logout'),

    # new create profile url
    path('create_profile', CreateProfileView.as_view(), name = 'create_profile_form'),

    # follow and like urls
    path('profile/<int:pk>/follow', FollowSelect.as_view(), name = "follow"),
    path('profile/<int:pk>/delete_follow', FollowDelete.as_view(), name = "follow_delete"),

    path('post/<int:pk>/like', LikeSelect.as_view(), name = "like"),
    path('post/<int:pk>/delete_like', LikeDelete.as_view(), name = "like_delete"),

    # all api paths
    path(r'api', ProfileAPIView.as_view()),
    path(r'api/profile', ProfileAPIView.as_view()),
    path(r'api/profilelist', ProfileListAPIView.as_view()),
    path(r'api/post', PostAPIView.as_view()),
    path(r'api/profile/<int:pk>/feed', FeedAPIView.as_view()),
    path(r'api/post/create', CreatePostAPIView.as_view()),

    path(r'api/login', LoginAPIView.as_view()),
]