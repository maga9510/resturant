# Generated by Django 4.0.6 on 2022-07-20 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=64, verbose_name='Product name'),
        ),
    ]
