# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-11 14:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('pharma', '0013_auto_20171110_1915'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchase',
            name='total',
            field=models.BigIntegerField(default=5),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='dealer',
            name='d_id',
            field=models.IntegerField(unique=True),
        ),
        migrations.AlterField(
            model_name='purchase',
            name='price',
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name='purchase',
            name='qty',
            field=models.BigIntegerField(),
        ),
    ]
