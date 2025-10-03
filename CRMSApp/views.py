from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "index.html")

def signUp(request):
    return render(request, "signUp.html")

def login(request):
    return render(request, "login.html")

def user_dash(request):
    return render(request, "USER/dash.html")

def file_complaint(request):
    return render(request, "USER/file-complaint.html")

