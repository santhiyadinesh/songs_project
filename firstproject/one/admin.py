from django.contrib import admin
from . models import Songs
from .models import UserProfile
from .models import Review

# Register your models here.

admin.site.register(Songs)
admin.site.register(UserProfile)
admin.site.register(Review)