# Generated by Django 2.2.3 on 2019-07-24 16:04

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reporter', '0013_auto_20190724_1159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='huc6',
            name='geometry',
            field=django.contrib.gis.db.models.fields.PolygonField(srid=4326),
        ),
        migrations.AlterField(
            model_name='huc8',
            name='geometry',
            field=django.contrib.gis.db.models.fields.PolygonField(srid=4326),
        ),
    ]
