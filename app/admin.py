from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django import forms
from .models import *

# Register your models here.

class AsignaturaAdmin(admin.ModelAdmin):
    list_display=('sigla', 'nombre')

class SeccionAdmin(admin.ModelAdmin):
    list_display=('numero','jornada', 'asignatura')

class CustomUserAdmin(admin.ModelAdmin):
    list_display=('email', 'first_name', 'last_name')

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Asignatura, AsignaturaAdmin)
admin.site.register(Seccion, SeccionAdmin)