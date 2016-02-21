# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dcp', '0002_auto_define_place_type_enum'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='sameAs',
            field=models.URLField(blank=True, help_text='URL identifying the organization in the IT Device Manager which possess it.'),
        ),
        migrations.AlterField(
            model_name='place',
            name='type',
            field=models.CharField(choices=[('RecyclingPoint', 'Recycling Point')], max_length=16, default='RecyclingPoint'),
        ),
    ]
