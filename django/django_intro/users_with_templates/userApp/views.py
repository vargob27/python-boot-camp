from django.shortcuts import render, redirect
from .models import *

# Create your views here.
def index(request):
    context = {
        "all_users": User.objects.all()
    }
    return render(request, 'home.html', context)

def add(request):
    if request.method == 'POST':
        User.objects.create(firstName=request.POST['firstName'], lastName=request.POST['lastName'], email=request.POST['email'], age=request.POST['age'])
    return redirect('/')