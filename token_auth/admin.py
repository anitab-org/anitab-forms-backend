from django.contrib.auth import get_user_model
from django.contrib import admin

# Register your models here.

User = get_user_model()

admin.site.register(User)
