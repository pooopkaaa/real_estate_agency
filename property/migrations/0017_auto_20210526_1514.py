# Generated by Django 2.2.20 on 2021-05-26 12:14

from django.db import migrations


def update_new_building_field(apps, schema_editor):
    construction_min_year = 2015
    Flat = apps.get_model('property', 'Flat')
    Flat.objects.filter(construction_year__lt=construction_min_year).update(new_building=None)


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0016_auto_20210525_1626'),
    ]

    operations = [
        migrations.RunPython(update_new_building_field)
    ]
