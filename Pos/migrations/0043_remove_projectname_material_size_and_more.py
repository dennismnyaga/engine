# Generated by Django 4.0.4 on 2024-11-04 20:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Pos', '0042_projectmaterial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projectname',
            name='material_size',
        ),
        migrations.RemoveField(
            model_name='projectname',
            name='material_to_use',
        ),
    ]