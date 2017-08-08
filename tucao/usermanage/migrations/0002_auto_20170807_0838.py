# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usermanage', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='telnumber',
            field=models.CharField(null=True, max_length=11),
        ),
        migrations.AlterField(
            model_name='user',
            name='born_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='head_img',
            field=models.TextField(null=True),
        ),
    ]
