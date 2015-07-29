# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WallPost',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pubdate', models.DateField(verbose_name=b'date published')),
                ('content', models.CharField(max_length=255)),
                ('author', models.CharField(max_length=50)),
            ],
        ),
    ]
