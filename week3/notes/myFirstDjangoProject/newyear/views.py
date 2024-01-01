from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.

def index(request):
    now = datetime.datetime.now()
    if now.month == 12 and now.day == 31:
        return render(request, "newyear/index.html", {
            "newyear": now.month == 12 and now.day == 31
        })
