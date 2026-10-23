#David Chung, dwjchung@bu.edu
#This is the urls file, in which we create the paths to the appropriate urls for our
#app, a show all page and individual show profile pages

from django.urls import path
from .views import ProfileListView, ProfileDetailView, PostDetailView, CreatePostView, UpdateProfileView, DeletePostView, UpdatePostView, ShowFollowersDetailView, ShowFollowingDetailView, ShowFeedView, SearchView

from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', ProfileListView.as_view(), name = "show_all_profiles"),
    path('profile/<int:pk>', ProfileDetailView.as_view(), name = 'show_profile'),
    path('post/<int:pk>', PostDetailView.as_view(), name = 'show_post'),
    path('post/<int:pk>/delete', DeletePostView.as_view(), name = 'delete'),
    path('post/<int:pk>/update', UpdatePostView.as_view(), name = 'update'),
    path('profile/<int:pk>/followers', ShowFollowersDetailView.as_view(), name = 'followers'),
    path('profile/<int:pk>/following', ShowFollowingDetailView.as_view(), name = 'following'),

    path('profile/feed', ShowFeedView.as_view(), name = "show_feed"),
    path('profile/search', SearchView.as_view(), name = "search"),
    path('profile/create_post', CreatePostView.as_view(), name = 'create_post'),
    path('profile/update', UpdateProfileView.as_view(), name = 'update_profile'),

    path('profile', ProfileDetailView.as_view(), name = 'show_profile'),

    path('login/', auth_views.LoginView.as_view(template_name = "mini_insta/login.html"), name = "login"),
    path('logout/', auth_views.LogoutView.as_view(next_page='show_all_profiles'), name='logout'),

]