from django.shortcuts import render
from django.http import HttpResponse
import os 

basedir = os.path.abspath(__file__)
parentdir = os.path.dirname(basedir)
maindir = os.path.dirname(parentdir)

# Create your views here.

def index(request):
    return HttpResponse("<h1>project05 index page</h1>")

def page2(request):
    content = os.path.join(maindir,"templates/inside_temp/sample.html")
    fp = open(content,"r")
    data = fp.read()
    return HttpResponse(data)

def page3(request):
    return render(request,"sample1.html")

