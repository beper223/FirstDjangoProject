from django.utils import timezone
from django.db.models import Count
from django.db.models.functions import ExtractWeekDay
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request

from src.taskmanager.dtos.task import TaskCreateSerializer, TaskListSerializer, TaskDetailSerializer
from src.taskmanager.models import Task, STATUS_CHOICES


class TaskListCreateView(APIView):
    def get(self, request: Request) -> Response:
        tasks = Task.objects.all()
        serializer = TaskListSerializer(tasks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request: Request) -> Response:
        serializer = TaskCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TaskDetailView(APIView):
    def get(self, request: Request, task_id: int) -> Response:
        try:
            task = Task.objects.get(pk=task_id)
        except Task.DoesNotExist:
            return Response({'error': 'Task not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = TaskDetailSerializer(task)
        return Response(serializer.data, status=status.HTTP_200_OK)


class TaskStatisticsView(APIView):
    def get(self, request: Request) -> Response:
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


class TasksByWeekdayView(APIView):
    def get(self, request: Request) -> Response:
        weekday = request.query_params.get('weekday')

        if weekday:
            try:
                weekday = int(weekday)
                if not 1 <= weekday <= 7:
                    raise ValueError
            except (ValueError, TypeError):
                return Response(
                    {'error': 'Параметр weekday должен быть числом от 1 (воскресенье) до 7 (суббота).'},
                    status=status.HTTP_400_BAD_REQUEST
                )

            tasks = Task.objects.annotate(
                weekday=ExtractWeekDay('created_at')
            ).filter(weekday=weekday)
            serializer = TaskListSerializer(tasks, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        else:
            days_map = {
                1: 'Воскресенье',
                2: 'Понедельник',
                3: 'Вторник',
                4: 'Среда',
                5: 'Четверг',
                6: 'Пятница',
                7: 'Суббота',
            }

            tasks_by_day = Task.objects.annotate(
                weekday=ExtractWeekDay('created_at')
            ).values('weekday').annotate(count=Count('id')).order_by('weekday')

            response_data = {
                days_map.get(item['weekday'], 'Неизвестный день'): item['count']
                for item in tasks_by_day
            }

            return Response(response_data, status=status.HTTP_200_OK)