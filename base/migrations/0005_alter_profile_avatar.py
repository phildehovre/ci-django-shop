# Generated by Django 4.2.11 on 2024-04-25 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_alter_profile_avatar_alter_profile_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(default='media/profile_pictures/default.jpg', upload_to='media/profile_pictures'),
        ),
    ]
