# Generated by Django 2.2.3 on 2019-07-24 15:59

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reporter', '0012_auto_20190724_1148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='huc6',
            name='geometry',
            field=django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326),
        ),
        migrations.AlterField(
            model_name='huc8',
            name='geometry',
            field=django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326),
        ),
    ]