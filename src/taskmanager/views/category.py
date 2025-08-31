from django.utils import timezone
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response

from src.taskmanager.models.task import Category
from src.taskmanager.dtos.category import CategorySerializer


class CategoryViewSet(ModelViewSet):

    queryset = Category.objects.filter(is_deleted=False)
    serializer_class = CategorySerializer

    def perform_destroy(self, instance):
        instance.is_deleted = True
        instance.deleted_at = timezone.now()
        instance.save(update_fields=['is_deleted', 'deleted_at'])

    @action(detail=False, methods=['get'], url_path='count-tasks')
    def count_tasks(self, request):
        # /api/v1/taskmanager/categories/count-tasks/
        # {
        #     "Categoty 1": 0,
        #     "Category 2": 0,
        #     "Category 3": 0,
        #     "Work": 0,
        #     "Work2": 1
        # }
        data = {
            category.name: category.tasks.count()
            for category in self.get_queryset()
        }
        return Response(data, status=status.HTTP_200_OK)
