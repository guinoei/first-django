# Generated by Django 5.0.1 on 2024-01-11 18:58

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0002_rename_record_taks'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Taks',
            new_name='Task',
        ),
    ]
