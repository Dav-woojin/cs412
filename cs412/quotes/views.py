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
    template_name = 'quote.html'
    context = {
    "rquote": quotelist[random.randint(0,2)],
    "rimage": imagelist[random.randint(0,2)],
    }
    return render(request, template_name, context)


def show_all(request):
    template_name = 'show_all.html'
    context = {
    "quotes": quotelist,
    "images": imagelist,
    }
    return render(request, template_name, context)

def about(request):
     
    #response_text = f'''
    #<html>
    #<h1>Hello, this is an about page dedicated to Maya Angelou, the speaker of these quotes</h1>

    #<p>Maya Angelou (1928–2014) was an iconic American poet, memoirist, and civil rights activist 
    #best known for her groundbreaking 1969 memoir, I Know Why the Caged Bird Sings.</p>
    #<p>This page was made by David Chung, a very middling full stack engineer at best</p>
    #</html>
    #'''

    template_name = 'about.html'
    context = {
    "rquote": quotelist[random.randint(0,2)],
    "rimage": imagelist[random.randint(0,2)],
    }
    return render(request, template_name, context)
 
