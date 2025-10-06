from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.index, name="index"),
    path("signUp/", views.signUp, name="signUp"),
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    
    # user
    path("user-dash/", views.user_dash, name="user-dash"),
    path("file-complaint/", views.file_complaint, name="file-complaint"),
    path("track-complaint/<int:id>", views.track_complaint, name="track-complaint"),
    path("user-profile/", views.user_profile, name="user-profile"),
    path("update-profile/", views.update_profile, name="update-profile"),
    path("update-password/", views.update_password, name="update-password"),
]

urlpatterns = urlpatterns+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)