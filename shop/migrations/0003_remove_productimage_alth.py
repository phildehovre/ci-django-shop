# Generated by Django 4.2.11 on 2024-06-06 09:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_productimage_alth'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productimage',
            name='alth',
        ),
    ]