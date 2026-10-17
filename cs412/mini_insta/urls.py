#David Chung, dwjchung@bu.edu
#This is the urls file, in which we create the paths to the appropriate urls for our
#app, a show all page and individual show profile pages

from django.urls import path
from .views import ProfileListView, ProfileDetailView, PostDetailView, CreatePostView, UpdateProfileView, DeletePostView, UpdatePostView, ShowFollowersDetailView, ShowFollowingDetailView


urlpatterns = [
    path('', ProfileListView.as_view(), name = "show_all_profiles"),
    path('profile/<int:pk>', ProfileDetailView.as_view(), name = 'show_profile'),
    path('post/<int:pk>', PostDetailView.as_view(), name = 'show_post'),
    path('profile/<int:pk>/create_post', CreatePostView.as_view(), name = 'create_post'),
    path('profile/<int:pk>/update', UpdateProfileView.as_view(), name = 'update_profile'),
    path('post/<int:pk>/delete', DeletePostView.as_view(), name = 'delete'),
    path('post/<int:pk>/update', UpdatePostView.as_view(), name = 'update'),
    path('profile/<int:pk>/followers', ShowFollowersDetailView.as_view(), name = 'followers'),
    path('profile/<int:pk>/following', ShowFollowingDetailView.as_view(), name = 'following'),
]