from rest_framework import serializers
from src.taskmanager.models import Task


class TaskCreateDTO(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = (
            'title',
            'description',
            'status',
            'deadline'
        )
