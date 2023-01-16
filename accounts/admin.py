from django.contrib import admin
from django.contrib.auth.views import LoginView

# Register your models here.
from rest_framework.authtoken.admin import TokenAdmin

TokenAdmin.raw_id_fields = ['user']
