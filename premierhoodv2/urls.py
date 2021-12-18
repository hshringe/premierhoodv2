"""premierhoodv2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path, include  # new
from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path("", views.index, name="index"),
    path("players/", views.listOfplayer, name="players"),
    path('players/<id>/', views.playerView, name='PlayerView'),
    path('players/<player_id>/impact', views.playerImpact, name='PlayerViewImpact'),
    path('players/<id>/creativity', views.playerCreativity, name='PlayerViewCreativity'),
    path('players/<player_id>/influence', views.playerInfluence, name='PlayerViewInfluence'),
    path('user/stocks', views.userStockView, name='UserStockView'),
    path("register", views.register_request, name="register"),
    path("login/", views.login_request, name="login")

]
