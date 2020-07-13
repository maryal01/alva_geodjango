# Generated by Django 2.2.3 on 2019-07-23 11:22

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reporter', '0007_delete_watershedshuc2'),
    ]

    operations = [
        migrations.CreateModel(
            name='WaterSheds',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('geometry', django.contrib.gis.db.models.fields.PolygonField(srid=4326)),
                ('name', models.CharField(max_length=255, unique=True)),
            ],
        ),
    ]