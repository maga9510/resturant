# Generated by Django 4.0.6 on 2022-09-05 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_alter_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='paymants',
            field=models.CharField(choices=[('Cash', 'Cash'), ('Terminal', 'Terminal'), ('PayMe', 'PayMe'), ('Click', 'Click')], max_length=10, verbose_name='Paymants'),
        ),
    ]
