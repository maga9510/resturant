# Generated by Django 4.0.6 on 2022-09-07 09:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0014_alter_product_view_day'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='count',
        ),
        migrations.AlterField(
            model_name='product_view',
            name='day',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 7, 14, 31, 14, 978133)),
        ),
    ]