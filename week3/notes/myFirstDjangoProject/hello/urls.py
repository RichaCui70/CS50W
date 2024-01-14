from django.urls import path
from . import views

#these are the allowed urls in my hello app. Must go blah/hello/whateverBelow
urlpatterns = [
    path("", views.index, name="helloworld"),
    path("/<str:name>", views.greet, name="greet"),
    path("/richard", views.richard, name="richard")
]