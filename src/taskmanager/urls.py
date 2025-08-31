from django.urls import path

from src.taskmanager.views.task import (
    TaskListCreateView,
    TaskDetailView,
    TaskStatisticsView,
    TasksByWeekdayView,
)
from src.taskmanager.views.subtask import SubTaskListCreateView, SubTaskDetailUpdateDeleteView

urlpatterns = [
    path('', TaskListCreateView.as_view()),
    path('tasks_by_weekday/', TasksByWeekdayView.as_view()),
    path('<int:task_id>/', TaskDetailView.as_view()),
    path('stats/', TaskStatisticsView.as_view()),
    path('subtasks/', SubTaskListCreateView.as_view(), name='subtask-list-create'),
    path('subtasks/<int:pk>/', SubTaskDetailUpdateDeleteView.as_view(), name='subtask-detail-update-delete'),
]