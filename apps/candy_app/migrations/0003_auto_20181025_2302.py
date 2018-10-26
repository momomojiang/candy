# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-10-25 23:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0003_auto_20181025_1753'),
        ('candy_app', '0002_auto_20181025_1753'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=125)),
                ('poster', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='created_message', to='login.User')),
            ],
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
