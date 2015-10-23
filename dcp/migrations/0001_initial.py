# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True,
                                        primary_key=True, verbose_name='ID')),
                ('label', models.CharField(
                            unique=True,
                            max_length=256,
                            help_text='Human friendly name of the Place'
                )),
                ('sameAs', models.URLField(
                            help_text='URL identifying the organization in '
                                      'the IT Device Manager which possess it.'
                )),
                ('geo', django.contrib.gis.db.models.fields.PolygonField(
                            srid=4326)
                ),
                ('type', models.CharField(max_length=16)),
            ],
        ),
    ]
