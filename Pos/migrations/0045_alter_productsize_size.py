# Generated by Django 4.0.4 on 2024-11-07 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pos', '0044_rename_projectmaterial_taskmaterial_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productsize',
            name='size',
            field=models.DecimalField(decimal_places=2, max_digits=50),
        ),
    ]
