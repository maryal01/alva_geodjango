# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-11 15:26
from __future__ import unicode_literals

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reporter', '0003_delete_counties'),
    ]

    operations = [
        migrations.CreateModel(
            name='Counties',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('counties', models.CharField(max_length=25)),
                ('codes', models.IntegerField()),
                ('cty_code', models.CharField(max_length=24)),
                ('dis', models.IntegerField()),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
            ],
        ),
    ]
