# Generated by Django 4.0 on 2024-06-11 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('capstone', '0002_group_time_and_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='time_and_date',
            field=models.DateTimeField(default=None),
        ),
    ]
