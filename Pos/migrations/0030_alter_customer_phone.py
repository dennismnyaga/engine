# Generated by Django 4.0.4 on 2024-10-07 01:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pos', '0029_salesanalytics_number_of_orders'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='phone',
            field=models.IntegerField(unique=True),
        ),
    ]
