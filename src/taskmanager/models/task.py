from django.db import models

STATUS_CHOICES = [
        ('new', 'New'),
        ('in_progress', 'In progress'),
        ('pending', 'Pending'),
        ('blocked', 'Blocked'),
        ('done', 'Done'),
]

class Category(models.Model):
    name = models.CharField(max_length=100)
    is_deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        unique_together = ('name', )
        db_table = "task_manager_category"
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class BaseTask(models.Model):
    title = models.CharField(
        max_length=65
    )
    description = models.TextField(
        blank=True
    )
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default=STATUS_CHOICES[0][0]
    )
    deadline = models.DateTimeField()
    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        abstract = True

    def __str__(self):
        return self.title

class Task(BaseTask):
    created_date = models.DateField(
        auto_now_add=True
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='tasks'
    )
    class Meta:
        unique_together = ('title',)
        db_table = "task_manager_task"
        verbose_name = "Task"
        verbose_name_plural = "Tasks"
        ordering = ['-created_at', 'title']

class SubTask(BaseTask):
    task = models.ForeignKey(
        'Task',
        on_delete=models.CASCADE,
        related_name="subtasks",
    )
    class Meta:
        unique_together = ('title', 'task')
        db_table = "task_manager_subtask"
        verbose_name = "SubTask"
        verbose_name_plural = "SubTasks"
        ordering = ['-created_at', 'title']
