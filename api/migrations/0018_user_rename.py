# Generated by Django 2.1.3 on 2018-11-19 20:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0017_auto_20181029_1921'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Member',
            new_name='User',
        ),
    ]