# Generated by Django 4.2.5 on 2023-09-19 13:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0012_delete_computerandphonebrand'),
    ]

    operations = [
        migrations.RenameField(
            model_name='clothe',
            old_name='size',
            new_name='sizes',
        ),
    ]
