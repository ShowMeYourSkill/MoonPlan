# Generated by Django 3.2.9 on 2021-12-11 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MoonPlanApp', '0002_groups'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groups',
            name='descriptions',
            field=models.CharField(blank=True, max_length=64),
        ),
    ]
