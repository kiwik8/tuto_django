# Generated by Django 3.2.5 on 2021-07-23 22:53

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_variety_stock'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='variety',
            name='prices',
        ),
        migrations.AddField(
            model_name='variety',
            name='price',
            field=models.IntegerField(default=10),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Price',
        ),
    ]
