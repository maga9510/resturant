# Generated by Django 4.0.6 on 2022-09-05 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.PositiveSmallIntegerField(choices=[('new', 'new'), ('pending', 'pending'), ('preparing', 'preparing'), ('cancellation', 'cancellation')], default=1, verbose_name='Order status'),
        ),
    ]
