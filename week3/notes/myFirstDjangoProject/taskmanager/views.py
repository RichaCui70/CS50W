from django.shortcuts import render
from django.http import HttpResponse


tasks = ["butt", "bar", "baz"]
# Create your views here.
def index(request):
    return render(request, "taskmanager/index.html", {
        "tasks": tasks
    })
