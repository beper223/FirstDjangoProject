# Generated by Django 5.2.3 on 2025-07-13 10:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=65)),
                ('description', models.TextField(blank=True)),
                ('status', models.CharField(choices=[('new', 'New'), ('in_progress', 'In progress'), ('pending', 'Pending'), ('blocked', 'Blocked'), ('done', 'Done')], default='new', max_length=20)),
                ('deadline', models.DateTimeField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('created_date', models.DateField(auto_now_add=True)),
                ('categories', models.ManyToManyField(related_name='tasks', to='taskmanager.category')),
            ],
            options={
                'unique_together': {('title', 'created_date')},
            },
        ),
        migrations.CreateModel(
            name='SubTask',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=65)),
                ('description', models.TextField(blank=True)),
                ('status', models.CharField(choices=[('new', 'New'), ('in_progress', 'In progress'), ('pending', 'Pending'), ('blocked', 'Blocked'), ('done', 'Done')], default='new', max_length=20)),
                ('deadline', models.DateTimeField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('created_date', models.DateField(auto_now_add=True)),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subtasks', to='taskmanager.task')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
