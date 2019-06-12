from django.contrib import admin

from WebSite.models import todolist, users

# Register your models here.

admin.site.register(todolist)
admin.site.register(users)