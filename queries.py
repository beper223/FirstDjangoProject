import os
import django
from datetime import timedelta
from django.utils import timezone


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from src.taskmanager.models import Task, SubTask


print("create Task: create 'Prepare presentation'")
presentation = Task.objects.create(
    title="Prepare presentation",
    description="Prepare materials and slides for the presentation",
    status="new",
    deadline=timezone.now() + timedelta(days=3),
)
print(presentation, presentation.id)

print("create SubTask: 'Gather information'")
gather_info = SubTask.objects.create(
    task=presentation,
    title="Gather information",
    description="Find necessary information for the presentation",
    status="new",
    deadline=timezone.now() + timedelta(days=2),
)
print(gather_info, gather_info.id)

print("create SubTask: 'Create slides'")
create_slides = SubTask.objects.create(
    task=presentation,
    title="Create slides",
    description="Create presentation slides",
    status="new",
    deadline=timezone.now() + timedelta(days=1),
)
print(create_slides,create_slides.id)

print("find all tasks with status 'New'")
new_tasks = Task.objects.filter(status="new")
for task in new_tasks:
    print(task.title, task.id, task.deadline, task.status)

print("Overdue subtasks with status 'Done'")
expired_done_subtasks = SubTask.objects.filter(
    status="done",
    deadline__lt=timezone.now(),
)
for subtask in expired_done_subtasks:
    print(subtask.title, subtask.id, subtask.deadline, subtask.status)

print("Task status 'Prepare presentation' → 'In progress'")
presentation.status = "in_progress"
presentation.save(update_fields=["status"])
print(presentation)

print("Gather information deadline → two days ago.")
gather_info.deadline = timezone.now() - timedelta(days=2)
gather_info.save(update_fields=["deadline"])
print(gather_info)

print("Description 'Create slides'")
create_slides.description = "Create and format presentation slides"
create_slides.save(update_fields=["description"])
print(create_slides)

# Удаляем задачу и все связанные подзадачи (CASCADE)
print("Delete the task and all related subtasks (CASCADE)")
presentation.delete()
tasks = Task.objects.filter(title="Prepare presentation")
print(tasks.count())