from django.shortcuts import render, redirect
from .models import AuthModel, Complaint
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

# Create your views here.

def logout(request):
    auth.logout(request)
    return redirect('/login/')

def index(request):
    return render(request, "index.html")

def signUp(request):
    if request.method == 'POST':
        full_name = request.POST.get("full_name")
        email = request.POST.get("email")
        phone_number = request.POST.get("phone_number")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")
        profilePicture = request.FILES.get("profilePicture")
        
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
                role='user', profile_img=profilePicture, username=email
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
    current_user = request.user
    complaints = Complaint.objects.filter(user=current_user)
    
    context = {
        "complaints": complaints
    }
    return render(request, "USER/dash.html", context)

def file_complaint(request):
    if request.method == 'POST':
        current_user = AuthModel.objects.filter(email=request.user).first()
        
        category = request.POST.get("category")
        description = request.POST.get("description")
        location = request.POST.get("location")
        attachment = request.FILES.get("attachment")
        
        if not category or not description:
            return JsonResponse({
                "message": "Sorry category and description are required!!",
                "success": False
            })
        
        else:
            Complaint.objects.create(
                user=current_user, complaint_category=category, description=description, location=location,
                complaint_files=attachment
            )
            return JsonResponse({
                "message": "Your Complaint has been filed successfully...",
                "success": True
            })
    return render(request, "USER/file-complaint.html")

view = False
def view_complaint(request, id):
    view = True
    complaint = Complaint.objects.filter(id=id).first()
    context = {
        "complaint": complaint,
        "view": view
    }
    return render(request, "USER/track-complaint.html", context)

def track_complaint(request, id):
    complaint = Complaint.objects.filter(id=id).first()
    context = {
        "complaint": complaint,
        "view": view
    }
    return render(request, "USER/track-complaint.html", context)

def user_profile(request):
    profile = request.user
    context = {
        "profile": profile
    }
    return render(request, "USER/profile.html", context)

def update_profile(request):
    if request.method == 'POST':
        current_user = request.user
        
        full_name = request.POST.get("full_name")
        phone_number = request.POST.get("phone_number")
        profilePicture = request.FILES.get("profilePicture")
        
        current_user.full_name = full_name
        current_user.phone_number = phone_number
        current_user.profile_img = profilePicture
        
        current_user.save()
        
        return JsonResponse({
            "message": "Profile Updated successfully...",
            "success": True
        })
            
    else:
        return redirect('/user-profile/')

def update_password(request):
    if request.method == 'POST':
        current_user = AuthModel.objects.filter(email=request.user).first()
        
        old_password = request.POST.get("old_password")
        new_password = request.POST.get("new_password")
        confirm_password = request.POST.get("confirm_password")
        
        if not current_user.check_password(old_password):
            return JsonResponse({
                "message": "Sorry this is not your current password!!",
                "success": False
            })
        
        elif confirm_password != new_password:
            return JsonResponse({
                "message": "Sorry you password and confirm password missed match!!",
                "success": False
            })
        
        else:
            current_user.set_password(new_password)
            current_user.save()
            auth.logout(request)
            return JsonResponse({
                "message": "Your password has been updated successfully...",
                "success": True
            })
        
    else:
        return redirect('/user-profile/')
