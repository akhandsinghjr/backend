# Generated by Django 4.1.5 on 2023-01-12 18:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.CharField(max_length=10, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('organizer', models.CharField(max_length=100)),
                ('venue', models.CharField(max_length=255)),
                ('start_time', models.DateTimeField(blank=True)),
                ('description', models.TextField()),
                ('end_time', models.DateTimeField(blank=True)),
                ('prize', models.CharField(max_length=150)),
                ('registration_fee', models.DecimalField(decimal_places=2, default=0, max_digits=8)),
                ('video', models.URLField(blank=True)),
                ('max_team_size', models.SmallIntegerField()),
                ('registration_deadline', models.DateTimeField(blank=True)),
                ('poster', models.URLField(blank=True)),
                ('tags', models.CharField(blank=True, choices=[('1', 'tech'), ('2', 'cultural'), ('3', 'sports'), ('4', 'gaming'), ('5', 'workshop'), ('6', 'other')], max_length=40)),
                ('min_team_size', models.SmallIntegerField()),
            ],
            options={
                'verbose_name': 'Event',
                'verbose_name_plural': 'Events',
                'ordering': ['start_time'],
            },
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('file', models.FileField(default=None, upload_to='static/gallery/')),
                ('type', models.CharField(choices=[('1', 'image'), ('2', 'video')], default='1', max_length=10)),
                ('tags', models.CharField(blank=True, choices=[('1', 'tech'), ('2', 'cultural'), ('3', 'sports'), ('4', 'gaming'), ('5', 'workshop'), ('6', 'other')], max_length=40)),
                ('timestamp', models.DateTimeField(default=datetime.datetime.now)),
            ],
            options={
                'verbose_name': 'Gallery',
                'verbose_name_plural': 'Gallery',
            },
        ),
    ]
