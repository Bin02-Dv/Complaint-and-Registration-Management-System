from django.contrib import admin
from .models import AuthModel, Complaint

# Register your models here.

admin.site.register(AuthModel)
admin.site.register(Complaint)
