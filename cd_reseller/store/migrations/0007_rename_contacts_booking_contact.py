# Generated by Django 3.2.5 on 2021-07-14 22:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_auto_20210715_0033'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='contacts',
            new_name='contact',
        ),
    ]
