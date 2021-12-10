from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic


def index(request):
    players = listOfplayer()
    return HttpResponse(players)

# Create your views here.

def listOfplayer():
    players = ['ronaldo ','ajay ','messi ','kante']
    return players