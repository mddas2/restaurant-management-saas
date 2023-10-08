# Generated by Django 4.2.5 on 2023-10-08 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TableAndSpace',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('status', models.CharField(choices=[('AV', 'Available'), ('OC', 'Occupied'), ('RE', 'Reserved')], default='AV', max_length=2)),
                ('capacity', models.IntegerField()),
                ('location', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True)),
                ('category', models.CharField(choices=[('SA', 'Sofa'), ('SP', 'Space'), ('BO', 'Booth'), ('BA', 'Bar'), ('OU', 'Outdoor'), ('PR', 'Private')], default='SP', max_length=20)),
            ],
        ),
    ]
