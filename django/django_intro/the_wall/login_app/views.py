from django.shortcuts import render, redirect
from django.contrib import messages, admin
from .models import *
import bcrypt

# Create your views here.
def index(request):
    return render(request, 'index.html')

def success(request):
    if 'user_id' not in request.session:
        return redirect('/')
    this_user = User.objects.filter(id=request.session['user_id'])
    context = {
        'user': this_user[0],
        'wall_messages': Wall_Message.objects.all()
    }
    return render(request, 'success.html', context)

def register(request):
    if request.method == 'POST':
        errors = User.objects.registration_validator(request.POST)
        if len(errors) != 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
    # hash password
        hashed_pw = bcrypt.hashpw(
            request.POST['password'].encode(), bcrypt.gensalt()).decode()
    # create User
        new_user = User.objects.create(
            first_name=request.POST['first_name'], last_name=request.POST[
                'last_name'], email=request.POST['email'], password=hashed_pw
        )
    # create session
        request.session['user_id'] = new_user.id
        return redirect('/success')
    return redirect('/')

def login(request):
    if request.method == "POST":
        errors = User.objects.login_validator(request.POST)
        if len(errors) != 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        this_user = User.objects.filter(email=request.POST['email'])
        request.session['user_id'] = this_user[0].id
        return redirect('/success')
    return redirect('/')

def logout(request):
    request.session.flush()
    return redirect('/')

def post(request):
    Wall_Message.objects.create(message=request.POST['post'], poster=User.objects.get(id=request.session['user_id']))
    return redirect('/success')

def comment(request, post_id):
    poster = User.objects.get(id=request.session['user_id'])
    message = Wall_Message.objects.get(id=post_id)
    Comment.objects.create(comment=request.POST['comment'], poster = poster, wall_message = message)
    return redirect('/success')

def profile(request, user_id):
    context = {
        'user': User.objects.get(id=user_id)
    }
    
    return render(request, 'profile.html', context)

def add_like(request, id):
    liked_message = Wall_Message.objects.get(id=id)
    user_liking = User.objects.get(id=request.session['user_id'])
    liked_message.user_likes.add(user_liking)
    return redirect('/success')