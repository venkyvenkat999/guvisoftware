from http.client import HTTPResponse
from django.shortcuts import render,redirect
from . models import *
from django.http import HttpResponse
from django.contrib.auth.models import User
from .forms import *
# Create your views here.
def index(request):
    return render(request,"a.html")
def homes(request):
    return render(request,"d.html")
def r(request):
    h=e()
    if request.method=="POST":
        name=request.POST["name"]
        #roll=request.POST["roll"]
        #college=request.POST["college"]
        password=request.POST["password"]
        #email=request.POST['email']
        #d=Register(name=name,password=password)
        #d.save()
        b=User.objects.create_user(username=name,password=password)
        b.save()
        return redirect("accounts/login")
    return render(request,"index2.html",{"e":h})