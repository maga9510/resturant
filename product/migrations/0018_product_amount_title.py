# Generated by Django 4.0.6 on 2022-09-13 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0017_delete_product_view'),
    ]

    operations = [
        migrations.AddField(
            model_name='product_amount',
            name='title',
            field=models.CharField(default='', max_length=64, verbose_name='Item title'),
            preserve_default=False,
        ),
    ]
