# Generated by Django 4.2.11 on 2024-05-09 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0016_alter_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default='https://www.eag-led.com/wp-content/uploads/2017/04/Product-Image-Coming-Soon.png', upload_to='media/products'),
        ),
    ]
