# Generated by Django 4.0.4 on 2023-10-17 23:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pos', '0014_alter_productpro_price_alter_stockproperty_extrasize_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employees',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='productpro',
            name='quantity',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
