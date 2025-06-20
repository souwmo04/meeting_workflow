# Generated by Django 5.2.3 on 2025-06-16 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Meeting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Meeting Name')),
                ('bot_name', models.CharField(max_length=100, verbose_name='Bot Name')),
                ('meeting_link', models.URLField(blank=True, verbose_name='Link')),
                ('join_time', models.TimeField(blank=True, null=True, verbose_name='Join Time')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
