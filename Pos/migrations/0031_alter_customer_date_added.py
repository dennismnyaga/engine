# Generated by Django 4.0.4 on 2024-10-18 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pos', '0030_alter_customer_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='date_added',
            field=models.DateTimeField(),
        ),
    ]
