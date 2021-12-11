from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic

from premierhoodv2.settings import AUTH_PASSWORD_VALIDATORS

from django.shortcuts import  render, redirect
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages
from django.shortcuts import  render, redirect
from .forms import NewUserForm
from django.contrib.auth import login, authenticate #add this
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm #add this

def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request,user)
			messages.success(request, "Registration successful." )
			return redirect("main:homepage")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="templates/register.html", context={"register_form":form})

def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("main:homepage")
			else:

				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="templates/login.html", context={"login_form":form})

def index(request):
    players = listOfplayer()
    return render(request=request, template_name="templates/home.html")


# Create your views here.

def listOfplayer():
    players = ['ronaldo ','ajay ','messi ','kante']
    return players



# def login(request):
#     username = request.POST.get('username', '')
#     password = request.POST.get('password', '')
#     user = AUTH_PASSWORD_VALIDATORS.authenticate(username=username, password=password)
#     if user is not None and user.is_active:
#         # Correct password, and the user is marked "active"
#         AUTH_PASSWORD_VALIDATORS.login(request, user)
#         # Redirect to a success page.
#     return render(request, 'admin/dashboard.html')  

def dashboard(request):
    return render(request, 'admin/dashboard.html') 