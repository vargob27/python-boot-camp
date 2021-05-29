from django.shortcuts import render
from time import localtime, strftime
# from time import gmtime, strftime

def index(request):
    # context = {
    #     "time": strftime("%Y-%m-%d %J:%M %p", gmtime())
    # }
    # return render(request,'index.html', context)
    context = {
        "date": strftime("%Y-%m-%d"),
        "time": strftime("%H:%M")
    }
    return render(request, 'index.html', context)

# Create your views here.
