from django.shortcuts import render
from django.urls import path
from hello import views



def home(request):
    return HttpResponse("Hello, Django!")

urlpatterns = [
    path("", views.home, name="home"),
]

# Create your views here.
