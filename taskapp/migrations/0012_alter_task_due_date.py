# Generated by Django 3.2.7 on 2022-01-10 02:43

from django.db import migrations, models
import taskapp.models


class Migration(migrations.Migration):

    dependencies = [
        ('taskapp', '0011_alter_item_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='due_date',
            field=models.DateField(default=taskapp.models.Task.default_date),
        ),
    ]
