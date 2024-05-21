# Generated by Django 4.2.11 on 2024-05-07 14:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0010_order_shipping'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.order'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default='https://www.eag-led.com/wp-content/uploads/2017/04/Product-Image-Coming-Soon.png', upload_to='products'),
        ),
    ]
