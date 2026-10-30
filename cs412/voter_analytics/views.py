from django.shortcuts import render

from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from . models import Voter
from datetime import date

import math
import plotly
import plotly.graph_objs as go

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

class GraphListView(ListView):
    model = Voter
    template_name = "voter_analytics/graphs.html"

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
        context["party_affils"] = ['U ', 'D ', 'R ', 'J ', 'A ', 'CC', 'X ', 'L ', 'Q ', 'S ', 'FF', 'G ', 'HH', 'T ', 'AA', 'GG', 'Z ', 'O ', 'P ', 'E ', 'V ', 'H ', 'Y ', 'W ', 'EE', 'K ']
        context['voterscores'] = ['0','1','2','3','4','5']
        context["years"] = [str(y) for y in range(1920, 2004)]
        context["priorvotes"] = ["v20state", "v21town", "v21primary", "v22general", "v23town"]

        voters = self.get_queryset()

        birth_dist = {}
        for y in range(1920, 2004):
            birth_dist[y] = sum([1 for x in voters.filter(DOB__year = y)])

        x = list(birth_dist.keys())
        y = list(birth_dist.values())

        fig = go.Bar(x=x, y=y)
        title_text = "Voter Distribution by Year of Birth"
        graph_div_birth = plotly.offline.plot({"data": [fig],
                                            "layout_title_text": title_text,
                                            }, auto_open=False, output_type="div",
                                            )


        context['graph_div_birth'] = graph_div_birth

        party_dist = {}
        for p in ['U ', 'D ', 'R ', 'J ', 'A ', 'CC', 'X ', 'L ', 'Q ', 'S ', 'FF', 'G ', 'HH', 'T ', 'AA', 'GG', 'Z ', 'O ', 'P ', 'E ', 'V ', 'H ', 'Y ', 'W ', 'EE', 'K ']:
            party_dist[p] = sum([1 for x in voters.filter(Party_Affiliation = p)])

        labels = list(party_dist.keys())
        values = list(party_dist.values())

        fig2 = go.Pie(labels=labels, values=values)
        title_text2 = "Voter Distribution by Party Affiliation"
        graph_div_party = plotly.offline.plot({"data": [fig2],
                                            "layout_title_text": title_text2,
                                            }, auto_open=False, output_type="div",
                                            )

        context['graph_div_party'] = graph_div_party 

        elect_dist = {}
        elect_dist["v20state"] = sum([1 for x in voters.filter(v20state = 'TRUE')])
        elect_dist["v21town"] = sum([1 for x in voters.filter(v21town = 'TRUE')])
        elect_dist["v21primary"] = sum([1 for x in voters.filter(v21primary = 'TRUE')])
        elect_dist["v22general"] = sum([1 for x in voters.filter(v22general = 'TRUE')])
        elect_dist["v23town"] = sum([1 for x in voters.filter(v23town = 'TRUE')])

        x2 = list(elect_dist.keys())
        y2 = list(elect_dist.values())

        fig3 = go.Bar(x=x2, y=y2)
        title_text = "Voter Distribution by Election"
        graph_div_elect = plotly.offline.plot({"data": [fig3],
                                            "layout_title_text": title_text,
                                            }, auto_open=False, output_type="div",
                                            )


        context['graph_div_elect'] = graph_div_elect

        return context
    