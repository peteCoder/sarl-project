# Generated by Django 4.2.9 on 2024-10-03 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_rename_countiriesvisited_countriesvisited_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='destination',
            old_name='trave_fee',
            new_name='travel_fee',
        ),
        migrations.AlterField(
            model_name='destination',
            name='other_details',
            field=models.CharField(max_length=100),
        ),
    ]
