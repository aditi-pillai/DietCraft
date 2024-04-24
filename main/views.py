from django.shortcuts import render
import requests

# Create your views here.


# Create your views here.

def home(response):
    return render(response, "main/home.html", {})

def dashboard(response):
    return render(response, "main/dashboard.html", {})