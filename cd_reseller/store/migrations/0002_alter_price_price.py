# Generated by Django 3.2.4 on 2021-06-29 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='price',
            name='price',
            field=models.IntegerField(),
        ),
    ]
