from django.contrib import admin

from src.taskmanager.models import (
    Category,
    Task,
    SubTask
)

class SubTaskInline(admin.TabularInline):
    model = SubTask
    extra = 1
    fields = ('title', 'description', 'status', 'deadline')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        'name'
    ]

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = [
        'short_title',
        'description',
        'status',
        'deadline'
    ]
    inlines = [SubTaskInline]

    @admin.display(description='Title')
    def short_title(self, obj):
        title = obj.title
        if len(title) > 10:
            return title[:10] + '...'
        return title



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
    actions = ['mark_done']

    @admin.action(description="Отметить как выполненные (Done)")
    def mark_done(self, request, queryset):
        updated = queryset.update(status='done')
        self.message_user(request, f"{updated} подзадач отмечены как выполненные.")