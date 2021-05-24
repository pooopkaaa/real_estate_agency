# Generated by Django 2.2.20 on 2021-05-24 12:50

from typing import Literal
from django.db import migrations

import phonenumbers


def update_owner_pure_phone(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    for flat in Flat.objects.all():
        parsed_number = phonenumbers.parse(flat.owners_phonenumber, 'RU')
        if phonenumbers.is_valid_number(parsed_number):            
            owner_pure_phone = f'+{parsed_number.country_code}{parsed_number.national_number}'
            flat.owner_pure_phone = owner_pure_phone
            flat.save()


def move_backward(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    for flat in Flat.objects.all():
        flat.owner_pure_phone = None
        flat.save()


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0008_auto_20210524_1547'),
    ]

    operations = [
        migrations.RunPython(update_owner_pure_phone, move_backward),
    ]