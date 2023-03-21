from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models

admin.site.register(models.Article)
admin.site.register(models.Reporter)
admin.site.register(models.Contact)
admin.site.register(models.MyUser, UserAdmin)
