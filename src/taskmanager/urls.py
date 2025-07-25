from django.urls import path

from src.taskmanager.views import (
    new_task,
    view_task,
    get_all_tasks,
    task_statistics
)

urlpatterns = [
    path('newtask/', new_task),
    path('', get_all_tasks),
    path('<int:task_id>/', view_task),
    path('stats/', task_statistics),
]