# Generated by Django 3.0.3 on 2020-02-09 11:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('taskreminder', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='taskmodel',
            old_name='tast_desc',
            new_name='task_desc',
        ),
    ]