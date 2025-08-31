from rest_framework import serializers
from src.taskmanager.models import SubTask
from src.taskmanager.dtos.validators import validate_deadline

class SubTaskCreateSerializer(serializers.ModelSerializer):
    deadline = serializers.DateTimeField(validators=[validate_deadline])
    class Meta:
        model = SubTask
        fields = (
            'title',
            'description',
            'status',
            'deadline',
            'task',
        )
        read_only_fields = ('created_at',)

class SubTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubTask
        fields = '__all__'