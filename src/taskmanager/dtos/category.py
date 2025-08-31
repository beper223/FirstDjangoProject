from rest_framework import serializers
from src.taskmanager.models import Category


class CategoryCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name',)

    def validate_name(self, value):
        qs = Category.objects.filter(name__iexact=value)
        if self.instance:
            qs = qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise serializers.ValidationError("Категория с таким названием уже существует.")
        return value

    def create(self, validated_data):
        self.validate_name(validated_data['name'])
        return super().create(validated_data)

    def update(self, instance, validated_data):
        if 'name' in validated_data:
            self.validate_name(validated_data['name'])
        return super().update(instance, validated_data)