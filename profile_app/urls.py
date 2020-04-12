"""ranking URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from . import views
from django.contrib import admin
from django.urls import path

from .views import (
    logout_views,
    #register_view,
    CreatePlayerView,
    PlayerView,
    PlayerListView,
    PlayerUpdateView,
    PlayerDeleteView,
    profileLogin,
    CreateJudgeView,
    JudgeUpdateView,
    JudgeDeleteView,
    JudgeListView


)
PlayerUpdateView
urlpatterns = [
    #path('login', views.login_view,name='login'),
    path('login', views.profileLogin.as_view(),name='login'),
    path('logout', views.logout_views,name='logout'),

    #Player Urls :

    #path('player/register', views.register_view,name='player/register'),
    path('player/register', CreatePlayerView.as_view(),name='RegisterPlayer'),
   # path('player/<int:id>', PlayerView.as_view(),name='PlayerView'),
    path('player/<int:id>', PlayerUpdateView.as_view(),name='PlayerView'),
    path('player/<int:id>/delete', PlayerDeleteView.as_view(),name='PlayerDelete'),
    path('player/list', PlayerListView.as_view(),name='PlayerListView'),

    #Judge Urls :
    path('judge/register', CreateJudgeView.as_view(),name='RegisterJudge'),
    path('judge/<int:id>', JudgeUpdateView.as_view(),name='JudgeView'),
    path('judge/<int:id>/delete', JudgeDeleteView.as_view(),name='JudgeDelete'),
    path('judge/list', JudgeListView.as_view(),name='JudgeListView'),
]