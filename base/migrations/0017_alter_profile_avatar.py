# Generated by Django 4.2.11 on 2024-06-25 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0016_alter_profile_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(upload_to='django_shop/profile_pictures'),
        ),
    ]
