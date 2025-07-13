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
    categories = models.ManyToManyField(
        'Category',
        related_name='tasks')
    created_date = models.DateField(
        auto_now_add=True
    )
    class Meta:
        # Из условия:
        # title: Название задачи. Уникально для даты.
        # В условии не сказано, для какой именно даты, поэтому берем пока created_date
        # К тому же непонятно, как из поля "дата+время" получить дату и подставить ее в unique_together
        unique_together = ('title', 'created_date')

class SubTask(BaseTask):
    task = models.ForeignKey(
        'Task',
        on_delete=models.CASCADE,
        related_name="subtasks",
    )

