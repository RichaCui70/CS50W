from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="helloworld"),
    path("<str:name>", views.greet, name="Greet"),
    path("richard", views.richard, name="richard")
]