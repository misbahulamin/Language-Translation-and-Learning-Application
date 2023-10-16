from django.contrib import admin
# from .models import User
from . import models

#admin.site.register(User)



@admin.register(models.RegisterModel)
class RegisterModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'roll' ]
    