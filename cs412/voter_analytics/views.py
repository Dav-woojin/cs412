from django.shortcuts import render

from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView
from . models import Voter

# Create your views here.

class ResultsListView(ListView):
    model = Voter
    template_name = 'voter_analytics/voters.html'
    context_object_name = 'voters'
    paginate_by = 100

    # def get_queryset(self):
    #     results = super().get_queryset()
    #     return results[:100]