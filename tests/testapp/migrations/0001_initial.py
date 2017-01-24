# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-06 10:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TestInline',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content1', models.TextField()),
                ('content2', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='TestPage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content1', models.TextField()),
                ('content2', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='testinline',
            name='page',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testapp.TestPage'),
        ),
    ]
