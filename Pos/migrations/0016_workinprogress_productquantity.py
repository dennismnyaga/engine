# Generated by Django 4.0.4 on 2023-10-18 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pos', '0015_alter_employees_email_alter_productpro_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='workinprogress',
            name='productQuantity',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
