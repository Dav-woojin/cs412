# urls.py file, define our paths for voter and graph and our main page
from django.urls import path
from .views import ResultsListView, ResultDetailView, GraphListView

urlpatterns = [
    path('', ResultsListView.as_view(), name = "voters"),
    path('voter/<int:pk>', ResultDetailView.as_view(), name = "voter_detail"),
    path('graphs', GraphListView.as_view(), name = "graphs")
]