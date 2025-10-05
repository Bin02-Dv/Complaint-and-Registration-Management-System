from django.shortcuts import render
from .models import AuthModel
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

# Create your views here.

def index(request):
    return render(request, "index.html")

def signUp(request):
    if request.method == 'POST':
        full_name = request.POST.get("full_name")
        email = request.POST.get("email")
        phone_number = request.POST.get("phone_number")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")
        
        if AuthModel.objects.filter(email=email).exists():
            return JsonResponse({
                "message": f"Sorry this email {email} already exist!!",
                "success": False
            })
        elif confirm_password != password:
            return JsonResponse({
                "message": "Sorry your password and confirm password missed!!",
                "success": False
            })
        else:
            AuthModel.objects.create_user(
                full_name=full_name, email=email, phone_number=phone_number, password=password,
                role='user'
            )
            return JsonResponse({
                "message": "Registration Completed successfully...",
                "success": True
            })
    return render(request, "signUp.html")

def login(request):
    if request.method == 'POST':
        email = request.POST.get("email")
        password = request.POST.get("password")
        
        user = AuthModel.objects.filter(email=email).first()
        
        url = ''
        
        if user is not None:
            if not user.check_password(password):
                return JsonResponse({
                    "message": "Sorry your password is incorrect!!",
                    "success": False
                })
            else:
                auth.login(request, user)
                if user.role == 'admin':
                    url = '/admin-dash/'
                else:
                    url = '/user-dash/'
                return JsonResponse({
                    "message": "Login successfully...",
                    "success": True,
                    "url": url
                })
        else:
            return JsonResponse({
                "message": f"Sorry we couldn't find any user with this email {email}",
                "success": False
            })
            
    return render(request, "login.html")

def user_dash(request):
    return render(request, "USER/dash.html")

def file_complaint(request):
    return render(request, "USER/file-complaint.html")

def track_complaint(request):
    return render(request, "USER/track-complaint.html")

def user_profile(request):
    return render(request, "USER/profile.html")
