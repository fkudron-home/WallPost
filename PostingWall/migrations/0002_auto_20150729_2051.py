# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('PostingWall', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wallpost',
            name='pubdate',
            field=models.DateTimeField(verbose_name=b'date published'),
        ),
    ]
