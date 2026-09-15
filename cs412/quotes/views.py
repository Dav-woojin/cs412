#David Chung, dwjchung@bu.edu
#this is the views.py file, in which we are trying to determine what exactly each template will do.

from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
import random

quotelist = ["Do the best you can until you know better. Then when you know better, do better.", 
             "I’ve learned that people will forget what you said, people will forget what you did, but people will never forget how you made them feel.",
             "You may not control all the events that happen to you, but you can decide not to be reduced by them.",
             ]

imagelist = ["https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT_CK-RrD3Q-CX4NHP4_4b_LGup1fkk0I8r7HTpsiJAig&s=10",
             "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcREhhQIy1oGrPILAcVtdLcMxmvlTnwM5iLrIZP1Ute7-Q&s=10",
             "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTYa5ZZKSuCK8wFLCyDP__34Tg7n66rhIWeMoS3h91tXg&s=10",
             ]
# Create your views here.

def quote(request):
    #This function returns quote.html as our template, while also providing context 
    #template variables that provide a random quote and image for quote.html to use
    template_name = 'quotes/quote.html'
    context = {
    "rquote": quotelist[random.randint(0,2)],
    "rimage": imagelist[random.randint(0,2)],
    }
    return render(request, template_name, context)


def show_all(request):
    #This function returns show_all.html as our template, while also providing context 
    #template variables that provide the entire lists of quotes and images for show_all.html to use
    template_name = 'quotes/show_all.html'
    context = {
    "quotes": quotelist,
    "images": imagelist,
    }
    return render(request, template_name, context)

def about(request):
    #This function returns about.html as our template
    template_name = 'quotes/about.html'
    return render(request, template_name)
 
