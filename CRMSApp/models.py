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
