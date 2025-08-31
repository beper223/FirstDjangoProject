from rest_framework import serializers
from src.taskmanager.models import Task
from src.taskmanager.dtos.subtask import SubTaskSerializer
from src.taskmanager.dtos.validators import validate_deadline


class TaskCreateSerializer(serializers.ModelSerializer):
    deadline = serializers.DateTimeField(validators=[validate_deadline])
    class Meta:
        model = Task
        fields = (
            'title',
            'description',
            'status',
            'deadline',
            'category',
        )

class TaskListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = (
            'id',
            'title',
            'status',
            'deadline',
            'category',
        )

class TaskDetailSerializer(serializers.ModelSerializer):
    subtasks = SubTaskSerializer(many=True, read_only=True)
    class Meta:
        model = Task
        fields = '__all__'
