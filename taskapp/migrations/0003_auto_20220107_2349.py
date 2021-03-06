# Generated by Django 3.2.7 on 2022-01-08 02:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskapp', '0002_auto_20220107_2345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='address',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=6, null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='item',
            field=models.ManyToManyField(null=True, to='taskapp.Item'),
        ),
    ]
