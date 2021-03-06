# Generated by Django 3.2.9 on 2021-12-11 12:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MoonPlanApp', '0003_alter_groups_descriptions'),
    ]

    operations = [
        migrations.CreateModel(
            name='PhoneNumber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Places',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cities', models.CharField(blank=True, max_length=64)),
                ('numbers', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MoonPlanApp.phonenumber')),
            ],
        ),
    ]
