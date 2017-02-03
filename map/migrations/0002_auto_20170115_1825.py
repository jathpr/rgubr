# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-15 15:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, verbose_name='title')),
                ('announce_text', models.TextField(blank=True, max_length=512, null=True, verbose_name='announce')),
                ('text', models.TextField(max_length=4096, verbose_name='text')),
                ('start_date', models.DateTimeField(blank=True, verbose_name='start at')),
                ('end_date', models.DateTimeField(blank=True, null=True, verbose_name='end at')),
            ],
            options={
                'ordering': ['-start_date'],
                'verbose_name_plural': 'articles',
                'verbose_name': 'article',
            },
        ),
        migrations.DeleteModel(
            name='Mark',
        ),
    ]
