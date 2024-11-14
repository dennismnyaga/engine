# Generated by Django 4.0.4 on 2024-11-14 13:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Pos', '0050_alter_productsize_size'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='TaskMaterial',
            new_name='ProjectMaterial',
        ),
        migrations.RemoveField(
            model_name='projectmaterial',
            name='task',
        ),
        migrations.AddField(
            model_name='projectmaterial',
            name='project',
            field=models.ForeignKey(default=5, on_delete=django.db.models.deletion.CASCADE, related_name='materials', to='Pos.projectname'),
            preserve_default=False,
        ),
    ]