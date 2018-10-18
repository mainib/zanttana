# todos/admin.py
from django.contrib import admin

from .models import Profile, Zantta, Lodging, Logistic, Msg

admin.site.register(Profile)
admin.site.register(Zantta)
admin.site.register(Lodging)
admin.site.register(Logistic)
admin.site.register(Msg)
