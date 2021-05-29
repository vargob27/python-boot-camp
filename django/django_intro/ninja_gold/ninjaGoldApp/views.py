from django.shortcuts import render, redirect
from time import localtime, strftime
import random

# Create your views here.
def index(request):
    if 'gold' not in request.session or 'activities' not in request.session:
        request.session['gold'] = 0
        request.session['activites'] = []
    context = {
        "activities":request.session['activites']
    }
    return render(request, "index.html", context)

def process_money(request):
    if request.method == 'POST':
        myGold = request.session['gold']
        location = request.POST['location']
        activities = request.session['activites']
        if location == 'farm':
            goldThisTurn = round(random.random() * 10 + 10)
            
        elif location == 'cave':
            goldThisTurn = round(random.random() * 5 + 5)
            
        elif location == 'house':
            goldThisTurn = round(random.random() * 3 + 2)
            
        else:
            winOrLose = round(random.random())
            if winOrLose == 1:
                goldThisTurn = round(random.random() * 50)
            else:
                goldThisTurn = (round(random.random() * 50) * -1)
        myGold += goldThisTurn
        request.session['gold'] = myGold
        date_format='%m/%d/%Y %H:%M:%S %Z'
        myTime = strftime(date_format)
        if goldThisTurn >= 0:
            str = f"Earned {goldThisTurn} from the {location} at {myTime}"
        else:
            goldThisTurn *= -1
            str = f"Lost {goldThisTurn} from the {location} at {myTime}"
        activities.insert(0, str)
        request.session['activities'] = activities

    return redirect("/")