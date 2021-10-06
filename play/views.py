from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from django.contrib.auth.models import User 

import json

from django.shortcuts import render, HttpResponse, redirect
# Create your views here.
def index(request):
    return render(request, "play/index.html")

def handLogin(request):
    if request.method=="POST":
        # Get the post parameters
        loginusername=request.POST['loginusername']
        loginpassword=request.POST['loginpassword']
        user=authenticate(username= loginusername, password= loginpassword)
        if user is not None:
            login(request, user)
            return redirect("loggedIn")
        else:
            messages.info(request, 'Invalid credentials. Please try again!')
            return redirect("index")
    return HttpResponse("index")

def loggedIn(request):
    return render(request,"play/loggedIn.html")

def signup_page(request):
    return render(request, "play/signup.html")

def signup_view(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["pass1"]
        mail = request.POST["email"]
        form = UserCreationForm(request.POST)
        user = User.objects.create_user(username=username,
                                    email=mail,
                                    password=password)
        login(request, user)
        # context ={
        #         "temp": menu.objects.all()
        #     }
        return redirect("loggedIn")
        #return render(request, "hello/verified.html",context)
        #return HttpResponseRedirect(reverse("index"))
        #return render(request, "users/user.html", context)
    else:
        return render(request, "play/index.html")
