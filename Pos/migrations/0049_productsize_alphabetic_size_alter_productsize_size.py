# Generated by Django 4.0.4 on 2024-11-12 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pos', '0048_alter_customer_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='productsize',
            name='alphabetic_size',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='productsize',
            name='size',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=50, null=True),
        ),
    ]
