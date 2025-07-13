from django.contrib import admin

from src.taskmanager.models import Category, Task, SubTask

admin.site.register(Category)
admin.site.register(Task)
admin.site.register(SubTask)
