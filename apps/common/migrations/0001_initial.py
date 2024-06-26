# Generated by Django 5.0.4 on 2024-04-28 10:58

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Appeal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_ad', models.DateTimeField(auto_now_add=True)),
                ('updated_ad', models.DateTimeField(auto_now=True)),
                ('description', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_ad', models.DateTimeField(auto_now_add=True)),
                ('updated_ad', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(upload_to='banner_image/')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_ad', models.DateTimeField(auto_now_add=True)),
                ('updated_ad', models.DateTimeField(auto_now=True)),
                ('degree', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(5)])),
                ('description', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Meeting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_ad', models.DateTimeField(auto_now_add=True)),
                ('updated_ad', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=255)),
                ('zoom_meeting_id', models.CharField(max_length=255)),
                ('start_time', models.DateTimeField()),
                ('duration', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
