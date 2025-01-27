# Generated by Django 2.2.20 on 2021-05-24 15:51

from django.db import migrations


def fill_owner_model(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    Owner = apps.get_model('property', 'Owner')

    for flat in Flat.objects.all():
        Owner.objects.get_or_create(owner=flat.owner, owners_phonenumber=flat.owners_phonenumber, owner_pure_phone=flat.owner_pure_phone)

class Migration(migrations.Migration):

    dependencies = [
        ('property', '0010_owner'),
    ]

    operations = [
        migrations.RunPython(fill_owner_model)
    ]
