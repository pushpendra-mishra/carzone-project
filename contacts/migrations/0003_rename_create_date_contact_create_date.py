# Generated by Django 3.2.5 on 2021-09-13 21:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0002_rename_contacts_contact'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='Create_date',
            new_name='create_date',
        ),
    ]
