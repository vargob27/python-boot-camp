from django.http.response import HttpResponse
from django.shortcuts import render, HttpResponse, redirect

def index(request):
    return render(request, 'index.html')

def submit(request):
    request.session['name'] = request.POST['name']
    request.session['dojo'] = request.POST['dojo']
    request.session['lang'] = request.POST['lang']
    request.session['comment'] = request.POST['comment']
    return redirect("/result")

def result(request):
    context = {}
    return render(request, 'result.html', context)
            # 'name': request.POST['name'],
            # 'dojo': request.POST['dojo'],
            # 'lang': request.POST['lang'],
            # 'comment': request.POST['comment'],

# I changed before submitting but returning this info in the context I could call the information in the HTML file by writing {{name}}, {{dojo}}, etc...