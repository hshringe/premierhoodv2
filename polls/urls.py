from django.urls import path

from ..premierhoodv2 import views

urlpatterns = [
    path('', views.index, name='index'),
]