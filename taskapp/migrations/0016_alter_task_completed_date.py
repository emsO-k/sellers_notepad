# Generated by Django 3.2.7 on 2022-01-19 03:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskapp', '0015_remove_task_due_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='completed_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
