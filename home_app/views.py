
from django.shortcuts import redirect, render
def home(request):
    return render(request,"index.html")

def login(request):
    return render(request,"login.html")    
    