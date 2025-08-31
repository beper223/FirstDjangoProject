from django.urls import path, include
from rest_framework.routers import DefaultRouter

from src.taskmanager.views.category import CategoryViewSet
from src.taskmanager.views.task import (
    TaskListCreateView,
    TaskDetailView,
    TaskStatisticsView,
    TasksByWeekdayView,
)
from src.taskmanager.views.subtask import SubTaskListCreateView, SubTaskDetailUpdateDeleteView

router = DefaultRouter()
router.register(r'categories', CategoryViewSet, basename='category')

urlpatterns = [
    path('', TaskListCreateView.as_view()),
    path('tasks_by_weekday/', TasksByWeekdayView.as_view()),
    path('<int:pk>/', TaskDetailView.as_view()),
    path('stats/', TaskStatisticsView.as_view()),
    path('subtasks/', SubTaskListCreateView.as_view(), name='subtask-list-create'),
    path('subtasks/<int:pk>/', SubTaskDetailUpdateDeleteView.as_view(), name='subtask-detail-update-delete'),
    path('', include(router.urls)),
]