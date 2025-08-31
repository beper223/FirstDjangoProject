from django.utils import timezone
from rest_framework import serializers

def validate_deadline(value):
    if value < timezone.now():
        raise serializers.ValidationError("Deadline не может быть в прошлом.")
    return value