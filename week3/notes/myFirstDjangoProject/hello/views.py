from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
#this is what defines what is put onto the screen depending on the urls and its method used
def index(request):
    return render(request, "hello/index.html")

def richard(request):
    return HttpResponse("Hello Richard!!")

def greet(request, name):
    return render(request, "hello/greet.html", {
        "name": name.capitalize()
    })