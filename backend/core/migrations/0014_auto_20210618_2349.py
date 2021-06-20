# Generated by Django 3.2.2 on 2021-06-18 18:19

import core.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_merge_0011_streaks_0012_alter_exercisecount_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='history',
            name='card_id',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='streaks',
            name='day_count',
            field=core.models.custom_booleanfield(),
        ),
    ]
