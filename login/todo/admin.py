from django.contrib import admin
from .models import Todo, Login

class TodoAdmin(admin.ModelAdmin):
  list = ('title', 'description', 'completed')

class LoginAdmin(admin.ModelAdmin):
  list = ('email', 'password', 'username')

admin.site.register(Todo, TodoAdmin)
admin.site.register(Login, LoginAdmin)