# Generated by Django 4.0.4 on 2024-11-02 15:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Pos', '0038_employees_id_number'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='levels',
            new_name='quantity',
        ),
    ]