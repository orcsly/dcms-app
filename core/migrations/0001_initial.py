# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-31 20:48
from __future__ import unicode_literals

import core.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Content',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('title', models.TextField(blank=True)),
                ('body', models.TextField(blank=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('start_date', models.DateTimeField(blank=True, null=True)),
                ('end_date', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Content',
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('file', models.ImageField(blank=True, height_field=b'height', upload_to=core.models.file_name, width_field=b'width')),
                ('height', models.PositiveIntegerField(blank=True, null=True)),
                ('width', models.PositiveIntegerField(blank=True, null=True)),
                ('content', models.ManyToManyField(related_name='images', to='core.Content')),
            ],
        ),
        migrations.CreateModel(
            name='LogEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('when', models.DateTimeField(auto_now_add=True)),
                ('action', models.TextField(choices=[(b'add', b'Created'), (b'edit', b'Modified'), (b'delete', b'Deleted')], default=b'add')),
                ('diff', models.TextField(blank=True)),
                ('content', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Content')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='content_logs', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Log Entry',
                'verbose_name_plural': 'Log Entries',
            },
        ),
    ]
