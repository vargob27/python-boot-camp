from django.shortcuts import render, redirect
from .models import *

# Create your views here.
def index(request):
    context = {
        "all_users": User.objects.all()
    }
    return render(request, 'home.html', context)

def add(request):
    
    return redirect('/')