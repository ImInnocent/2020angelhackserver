from django.contrib import admin
from .models import Message, UserData

# Register your models here.
admin.site.register(Message)
admin.site.register(UserData)