# Generated by Django 4.2.5 on 2023-10-02 06:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tenant', '0005_resturentawaremodel'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ResturentAwareModel',
        ),
    ]
