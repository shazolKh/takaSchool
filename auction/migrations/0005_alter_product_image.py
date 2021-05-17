# Generated by Django 3.2.3 on 2021-05-17 17:26

import auction.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0004_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default='product/placeholder.png', upload_to=auction.models.image_path),
        ),
    ]
