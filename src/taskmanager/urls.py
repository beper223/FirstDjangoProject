from django.urls import path

from src.taskmanager.views import (
    new_task,
    view_task,
    get_all_tasks
)

urlpatterns = [
    path('newtask/', new_task, name='get_all_projects'),
    path('', get_all_tasks, name='get_all_tasks'),
    path('<int:task_id>/', view_task, name='view_task'),

]