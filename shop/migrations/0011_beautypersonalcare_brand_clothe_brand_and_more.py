# Generated by Django 4.2.5 on 2023-09-18 15:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0010_accessories_beautypersonalcarebrand_clothebrand_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='beautypersonalcare',
            name='brand',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.beautypersonalcarebrand'),
        ),
        migrations.AddField(
            model_name='clothe',
            name='brand',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.clothebrand'),
        ),
        migrations.AddField(
            model_name='homeliving',
            name='brand',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.homelivingbrand'),
        ),
        migrations.AddField(
            model_name='sportsoutdoors',
            name='brand',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.sportsoutdoorsbrand'),
        ),
        migrations.AddField(
            model_name='toysgames',
            name='brand',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.sportsoutdoorsbrand'),
        ),
        migrations.AlterField(
            model_name='beautypersonalcare',
            name='skin_type',
            field=models.CharField(choices=[('normal', 'Normal'), ('dry', 'Dry'), ('oily', 'Oily'), ('combination', 'Combination'), ('sensitive', 'Sensitive')], default='normal', max_length=20),
        ),
    ]
