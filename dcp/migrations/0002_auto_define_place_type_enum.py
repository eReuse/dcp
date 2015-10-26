# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dcp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='type',
            field=models.CharField(
                max_length=16,
                choices=[('RecyclingPoint', 'Recycling Point')]
            ),
        ),
    ]
