# Generated by Django 3.2.4 on 2023-02-12 03:22

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_auto_20230212_0838'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='updated_date',
            field=models.DateField(default=datetime.datetime(2023, 2, 12, 3, 22, 28, 793617, tzinfo=utc)),
        ),
    ]