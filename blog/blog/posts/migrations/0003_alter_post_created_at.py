# Generated by Django 4.1.2 on 2022-10-24 17:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_rename_create_at_post_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_at',
            field=models.DateTimeField(blank=b'I00\n', default=datetime.datetime.now),
        ),
    ]
