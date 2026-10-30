from django.urls import path
from .views import ResultsListView, ResultDetailView

urlpatterns = [
    path('', ResultsListView.as_view(), name = "voters"),
    path('voter/<int:pk>', ResultDetailView.as_view(), name = "voter_detail")
]