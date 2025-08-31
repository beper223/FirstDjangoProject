from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination

from src.taskmanager.models import SubTask
from src.taskmanager.dtos.subtask import (
    SubTaskSerializer,
    SubTaskCreateSerializer,
)


class SubTaskListCreateView(APIView):
    def get(self, request):
        paginator = PageNumberPagination()
        paginator.page_size = 5

        subtasks = SubTask.objects.all().order_by('-created_at')

        task_title = request.query_params.get('task_title')
        status_param = request.query_params.get('status')

        if task_title:
            subtasks = subtasks.filter(task__title=task_title)
        if status_param:
            subtasks = subtasks.filter(status=status_param)

        result_page = paginator.paginate_queryset(subtasks, request)
        serializer = SubTaskSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request):
        serializer = SubTaskCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SubTaskDetailUpdateDeleteView(APIView):
    def get_object(self, pk):
        try:
            return SubTask.objects.get(pk=pk)
        except SubTask.DoesNotExist:
            return None

    def get(self, request, pk):
        subtask = self.get_object(pk)
        if not subtask:
            return Response({'error': 'SubTask not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = SubTaskSerializer(subtask)
        return Response(serializer.data)

    def update(self, request, pk, partial=False):
        subtask = self.get_object(pk)
        if not subtask:
            return Response({'error': 'SubTask not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = SubTaskCreateSerializer(subtask, data=request.data, partial=partial)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        return self.update(request, pk, partial=False)

    def patch(self, request, pk):
        return self.update(request, pk, partial=True)

    def delete(self, request, pk):
        subtask = self.get_object(pk)
        if not subtask:
            return Response({'error': 'SubTask not found'}, status=status.HTTP_404_NOT_FOUND)
        subtask.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

