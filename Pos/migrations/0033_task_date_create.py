# Generated by Django 4.0.4 on 2024-10-20 16:13

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Pos', '0032_projectname_alter_customer_date_added_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date_create',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2024, 10, 20, 16, 13, 22, 317507, tzinfo=utc)),
            preserve_default=False,
        ),
    ]