# Generated by Django 2.0.7 on 2018-07-28 04:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_user_creation_date'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='App_User',
        ),
    ]