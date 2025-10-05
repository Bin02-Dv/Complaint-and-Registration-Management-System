from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("signUp/", views.signUp, name="signUp"),
    path("login/", views.login, name="login"),
    
    # user
    path("user-dash/", views.user_dash, name="user-dash"),
    path("file-complaint/", views.file_complaint, name="file-complaint"),
    path("track-complaint/", views.track_complaint, name="track-complaint"),
    path("user-profile/", views.user_profile, name="user-profile"),
]
