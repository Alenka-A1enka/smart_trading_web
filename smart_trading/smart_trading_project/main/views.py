from django.shortcuts import render
from .models import Users
from django.contrib.auth.models import User

def index(request):
    return render(request, 'main/index.html')