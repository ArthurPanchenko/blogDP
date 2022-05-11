from django.contrib import admin
from .models import CustomUser


@admin.register(CustomUser)
class PostAdmin(admin.ModelAdmin):
    model = CustomUser
    
