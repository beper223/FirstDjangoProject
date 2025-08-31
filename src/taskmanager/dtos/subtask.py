from rest_framework import serializers
from src.taskmanager.models import SubTask

class SubTaskCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubTask
        fields = (
            'title',
            'description',
            'status',
            'deadline',
        )
        read_only_fields = ('created_at',)

class SubTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubTask
        fields = '__all__'