# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-04-05 08:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bloodbank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
                ('contact', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
                ('owner', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('user_id', models.CharField(max_length=20)),
                ('pswd', models.CharField(max_length=20)),
                ('location', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=50)),
                ('numdon', models.CharField(max_length=10)),
                ('age', models.CharField(max_length=5)),
            ],
        ),
    ]
