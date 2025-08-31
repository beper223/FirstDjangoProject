from rest_framework import serializers
from src.taskmanager.models import Task, SubTask, Category
from src.taskmanager.dtos.subtask import SubTaskSerializer


class TaskCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = (
            'title',
            'description',
            'status',
            'deadline',
        )

class TaskListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = (
            'id',
            'title',
            'status',
            'deadline',
        )

class TaskDetailSerializer(serializers.ModelSerializer):
    subtasks = SubTaskSerializer(many=True, read_only=True)
    class Meta:
        model = Task
        fields = '__all__'
