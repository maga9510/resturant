# Generated by Django 4.0.6 on 2022-07-27 09:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_product_photo_alter_category_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='photo',
        ),
    ]
