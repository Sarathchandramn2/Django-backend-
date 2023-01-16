from django.contrib import admin

# Register your models here.
from .models  import movie

models_list=[movie]
admin.site.register(models_list)