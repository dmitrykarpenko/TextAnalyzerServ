from django.contrib import admin

from .models import User, UserText

admin.site.register(User)
admin.site.register(UserText)
