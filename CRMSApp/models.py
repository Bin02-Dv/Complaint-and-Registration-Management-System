from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class AuthModel(AbstractUser):
    full_name = models.CharField(max_length=100, blank=True)
    email = models.EmailField(max_length=200, blank=True, unique=True)
    phone_number = models.CharField(max_length=20, blank=True)
    profile_img = models.ImageField(upload_to='profile/', blank=True)
    role = models.CharField(max_length=20, blank=True)
    
    username = models.CharField(max_length=100, blank=True, unique=True)
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []
    
    def __str__(self):
        return self.full_name


class Complaint(models.Model):
    
    user = models.ForeignKey(AuthModel, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, blank=True)
    complaint_category = models.CharField(max_length=50, blank=True)
    description = models.TextField(max_length=250, blank=True)
    location = models.CharField(max_length=50, blank=True)
    
    complaint_files = models.ImageField(upload_to='complaints/', blank=True)
    date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=50, default='pending')
    
    def __str__(self):
        return self.description
