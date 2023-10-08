# Generated by Django 4.2.5 on 2023-10-08 06:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tenant', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FoodItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('description', models.TextField(blank=True)),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tenant.restaurant')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='MenuCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('food_item', models.ManyToManyField(blank=True, related_name='menu_category', to='management.fooditem')),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tenant.restaurant')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='FoodCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('food_item', models.ManyToManyField(blank=True, related_name='food_category', to='management.fooditem')),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tenant.restaurant')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
