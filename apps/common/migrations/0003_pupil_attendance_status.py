# Generated by Django 4.1 on 2024-03-29 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pupil',
            name='attendance_status',
            field=models.CharField(choices=[('Keldi', 'Keldi'), ('Kelmadi', 'Kelmadi')], default='Keldi', max_length=7, verbose_name='Davomat'),
        ),
    ]
