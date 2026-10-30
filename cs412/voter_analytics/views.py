from django.shortcuts import render

from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from . models import Voter
from datetime import date

# Create your views here.

class ResultsListView(ListView):
    model = Voter
    template_name = 'voter_analytics/voters.html'
    context_object_name = 'voters'
    paginate_by = 100

    def get_queryset(self):
        results = super().get_queryset()

        if 'party_affiliation' in self.request.GET:
            pa = self.request.GET['party_affiliation']
            if pa:
                results = results.filter(Party_Affiliation = pa)

        if 'voter_score' in self.request.GET:
            vs = self.request.GET['voter_score']
            if vs:
                results = results.filter(voter_score = vs)

        if 'min_dob_year' in self.request.GET:
            mdy = self.request.GET['min_dob_year']
            if mdy:
                results = results.filter(DOB__year__gt = int(mdy))

        if 'max_dob_year' in self.request.GET:
            mady = self.request.GET['max_dob_year']
            if mady:
                results = results.filter(DOB__year__lt = int(mady))

        if 'v20state' in self.request.GET:
            v1 = self.request.GET['v20state']
            if v1 and v1 == "on":
                results = results.filter(v20state = 'TRUE')

        if 'v21town' in self.request.GET:
            v21 = self.request.GET['v21town']
            if v21 and v21 == "on":
                results = results.filter(v21town = 'TRUE')

        if 'v21primary' in self.request.GET:
            v21p = self.request.GET['v21primary']
            if v21p and v21p == "on":
                results = results.filter(v21primary = 'TRUE')

        if 'v22general' in self.request.GET:
            v22g = self.request.GET['v22general']
            if v22g and v22g == "on":
                results = results.filter(v22general = 'TRUE')

        if 'v23town' in self.request.GET:
            v23 = self.request.GET['v23town']
            if v23 and v23 == "on":
                results = results.filter(v23town = 'TRUE')

        print("RESULT COUNT", results.count())
        return results

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context["filter"] = self.request.GET
        context["party_affils"] = ['U ', 'D ', 'R ', 'J ', 'A ', 'CC', 'X ', 'L ', 'Q ', 'S ', 'FF', 'G ', 'HH', 'T ', 'AA', 'GG', 'Z ', 'O ', 'P ', 'E ', 'V ', 'H ', 'Y ', 'W ', 'EE', 'K ']
        context['voterscores'] = ['0','1','2','3','4','5']
        context["years"] = [str(y) for y in range(1920, 2004)]
        context["priorvotes"] = ["v20state", "v21town", "v21primary", "v22general", "v23town"]
        return context

class ResultDetailView(DetailView):
    model = Voter
    context_object_name = 'v'
    template_name = "voter_analytics/voter_detail.html"