from django.contrib import admin

from src.taskmanager.models import (
    Category,
    Task,
    SubTask
)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        'name'
    ]

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'description',
        'status',
        'deadline',
        'created_at',
        'created_date'
    ]

@admin.register(SubTask)
class SubTaskAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'description',
        'status',
        'deadline',
        'created_at',
        'task'
    ]
