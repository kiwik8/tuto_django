# Generated by Django 3.2.5 on 2021-07-14 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_rename_contacts_booking_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='variety',
            name='stock',
            field=models.IntegerField(null=True),
        ),
    ]