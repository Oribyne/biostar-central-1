# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-19 19:39
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import engine.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Analysis',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('text', models.TextField(default='text')),
                ('summary', models.TextField(default='summary')),
                ('html', models.TextField(default='html')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('json_text', models.TextField(default='{}')),
                ('template', models.TextField(default='makefile')),
                ('valid', models.BooleanField(default=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('text', models.TextField(default='text')),
                ('html', models.TextField(default='html')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('type', models.IntegerField(choices=[(1, 'File'), (2, 'Collection')], default=1)),
                ('data_type', models.IntegerField(default=0)),
                ('size', models.CharField(max_length=256, null=True)),
                ('file', models.FileField(null=True, upload_to=engine.models.directory_path)),
                ('path', models.FilePathField(null=True)),
                ('valid', models.BooleanField(default=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('text', models.TextField(default='text')),
                ('summary', models.TextField(default='summary')),
                ('html', models.TextField(default='html')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('json_text', models.TextField(default='commands')),
                ('uid', models.CharField(max_length=32)),
                ('template', models.TextField(default='makefile')),
                ('log', models.TextField(default='No data logged for current job')),
                ('valid', models.BooleanField(default=True)),
                ('state', models.IntegerField(choices=[(1, 'Queued'), (2, 'Running'), (3, 'Finished'), (4, 'Error')], default=1)),
                ('path', models.FilePathField(default='')),
                ('analysis', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='engine.Analysis')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('text', models.TextField(default='text')),
                ('html', models.TextField(default='html')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('uid', models.CharField(max_length=32)),
                ('valid', models.BooleanField(default=True)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.Group')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='job',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='engine.Project'),
        ),
        migrations.AddField(
            model_name='data',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='engine.Project'),
        ),
        migrations.AddField(
            model_name='analysis',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='engine.Project'),
        ),
    ]
