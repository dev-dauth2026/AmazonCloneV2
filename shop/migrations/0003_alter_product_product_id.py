# Generated by Django 4.2.5 on 2023-09-15 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_product_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False),
        ),
    ]
