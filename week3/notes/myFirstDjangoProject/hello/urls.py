from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="helloworld"),
    path("/richard", views.richard, name="richard")
]