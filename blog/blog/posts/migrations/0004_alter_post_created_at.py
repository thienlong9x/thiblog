# Generated by Django 4.1.2 on 2022-10-24 17:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_alter_post_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_at',
            field=models.DateTimeField(blank=b'I01\n', default=datetime.datetime.now),
        ),
    ]
