# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=10)),
                ('password', models.CharField(max_length=16)),
                ('born_date', models.DateTimeField()),
                ('gender', models.BooleanField()),
                ('description', models.TextField(null=True, blank=True)),
                ('head_img', models.TextField()),
                ('exp', models.IntegerField()),
                ('rank', models.IntegerField()),
            ],
        ),
    ]
