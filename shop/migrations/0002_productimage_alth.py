# Generated by Django 4.2.11 on 2024-06-06 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='productimage',
            name='alth',
            field=models.CharField(default='default', max_length=150),
            preserve_default=False,
        ),
    ]