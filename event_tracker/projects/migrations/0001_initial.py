# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2019-05-24 05:49
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
                ('idea', models.CharField(max_length=150)),
                ('status', models.CharField(choices=[('ongoing', 'OnGoing'), ('completed', 'Completed'), ('onhold', 'OnHold')], max_length=9)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('project_head', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
