# Generated by Django 4.0.6 on 2022-09-07 13:38

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0004_order_last_name_order_name_order_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='craete_add',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2022, 9, 7, 13, 38, 5, 314959, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
