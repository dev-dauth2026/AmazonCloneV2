# Generated by Django 4.2.5 on 2023-09-21 16:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0014_clothesize_remove_clothe_sizes_clothe_sizes'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]
