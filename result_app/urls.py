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
    CreateResultView,
    ResultUpdateView,
    ResultDeleteView,
    ResultListView,
    resultUploadFileView,
    ResultCompatitionListView

)

urlpatterns = [

    path('upload', resultUploadFileView.as_view(),name='UploadResult'),
    path('create', CreateResultView.as_view(),name='CreateResult'),
    path('<int:id>', ResultUpdateView.as_view(),name='ResultView'),
    path('<int:id>/delete', ResultDeleteView.as_view(),name='ResultDelete'),
    path('list', ResultListView.as_view(),name='ResultListView'),
    path('compatition/<int:id>', ResultCompatitionListView.as_view(),name='ResultCompatitionListView'),
]