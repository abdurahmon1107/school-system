# Generated by Django 5.0.3 on 2024-03-16 13:17

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('common', '0002_delete_user'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('subject_name', models.CharField(max_length=250, verbose_name='Subject name')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('school_name', models.CharField(max_length=250)),
                ('adress', models.CharField(max_length=300)),
                ('director', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='school_director', to=settings.AUTH_USER_MODEL, verbose_name='Director')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
