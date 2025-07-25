from django.utils import timezone
from django.db.models import Count
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status

from src.taskmanager.dtos.task import TaskCreateSerializer, TaskListSerializer, TaskDetailSerializer
from src.taskmanager.models import Task, STATUS_CHOICES

@api_view(['POST'])
def new_task(request) -> Response:
    serializer = TaskCreateSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors,
        status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def view_task(request, task_id) -> Response:
    try:
        task = Task.objects.get(pk=task_id)
    except Task.DoesNotExist:
        return Response({'error': 'Book not found'},
                        status=status.HTTP_404_NOT_FOUND)
    serializer = TaskDetailSerializer(task)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_all_tasks(request) -> Response:
    tasks = Task.objects.all()
    serializer = TaskListSerializer(tasks, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def task_statistics(request) -> Response:
    total_tasks = Task.objects.count()

    raw_counts = Task.objects.values('status').annotate(count=Count('id'))
    status_map = dict(STATUS_CHOICES)
    status_data = {status_map.get(item['status'], item['status']): item['count'] for item in raw_counts}

    overdue_tasks = Task.objects.filter(
        deadline__lt=timezone.now()
    ).exclude(status='done').count()

    return Response({
        "total_tasks": total_tasks,
        "tasks_by_status": status_data,
        "overdue_tasks": overdue_tasks,
    }, status=status.HTTP_200_OK)