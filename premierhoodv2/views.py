from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic

from premierhoodv2.settings import AUTH_PASSWORD_VALIDATORS

from django.shortcuts import render, redirect
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate  # add this
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm  # add this
from django.db import connection
from .models import *


def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            email = form.cleaned_data.get('email')
            print(username)
            print(password)
            print(email)
            # THIS IS WHERE IT SHOULD PUSH TO A DATABASE
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("/players")
        messages.error(request, "Unsuccessful registration. Invalid information.")

    form = NewUserForm()
    return render(request=request, template_name="templates/register.html", context={"register_form": form})


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
                # GET THE USER FROM OUR OWN DATABASE
                return redirect("/players")
            else:

                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="templates/login.html", context={"login_form": form})


def index(request):
    return render(request=request, template_name="templates/home.html")


def listOfplayer(request):
    players = Player.objects.all()
    context = {'players': players}

    return render(request, 'templates/players.html', context)


def playerView(request, id):
    player = Player.objects.get(id=id)
    context = {"player": player}
    print(request.user)

    return render(request, 'templates/playerView.html', context)


def playerCreativity(request, player_id):
    player = Player.objects.get(id=player_id)
    stockCreativity = Stock_Creativity.objects.get(player_id=player_id)
    context = {
        "stock": stockCreativity,
        "type": "creativity",
        "player": player,
    }
    return render(request, 'templates/stockView.html', context)


def playerInfluence(request, player_id):
    player = Player.objects.get(id=player_id)
    stockInfluence = Stock_Influence.objects.get(player_id=player_id)
    context = {
        "stock": stockInfluence,
        "player": player,
        "type": "influence"
    }
    return render(request, 'templates/stockView.html', context)


def playerImpact(request, player_id):
    player = Player.objects.get(id=player_id)
    stockImpact = Stock_Impact.objects.get(player_id=player_id)
    context = {
        "stock": stockImpact,
        "type": "impact",
        "player": player,
    }
    return render(request, 'templates/stockView.html', context)


def buyCreativity(request, player_id):
    player = Player.objects.get(id=player_id)
    # post stock into user's stocks

    return HttpResponse("You just bought " + player.first_name +
                        " " + player.last_name + "'s Creativity ")


def buyImpact(request, player_id):
    player = Player.objects.get(id=player_id)
    # post stock into user's stocks

    return HttpResponse("You just bought " + player.first_name +
                        " " + player.last_name + "'s Impact ")


def buyInfluence(request, player_id):
    player = Player.objects.get(id=player_id)
    # post stock into user's stocks

    return HttpResponse("You just bought " + player.first_name +
                        " " + player.last_name + "'s Influence ")


def sellCreativity(request, player_id):
    player = Player.objects.get(id=player_id)
    # remove stock from user's stocks

    return HttpResponse("You just sold " + player.first_name +
                        " " + player.last_name + "'s Creativity ")


def sellImpact(request, player_id):
    player = Player.objects.get(id=player_id)
    # remove stock user's stocks

    return HttpResponse("You just sold " + player.first_name +
                        " " + player.last_name + "'s Impact ")


def sellInfluence(request, player_id):
    player = Player.objects.get(id=player_id)
    # remove stock user's stocks

    return HttpResponse("You just sold " + player.first_name +
                        " " + player.last_name + "'s Influence ")


def dashboard(request):
    return render(request, 'admin/dashboard.html')
