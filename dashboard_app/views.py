from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    context = {"dashboard_page": "active"}
    return render(request,'dashboard.html',context)