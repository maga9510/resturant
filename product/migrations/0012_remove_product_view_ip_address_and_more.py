# Generated by Django 4.0.6 on 2022-09-05 10:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0011_alter_product_view_day'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product_view',
            name='ip_address',
        ),
        migrations.AlterField(
            model_name='product_view',
            name='day',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 5, 15, 22, 27, 730213)),
        ),
    ]
