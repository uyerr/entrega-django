# Generated by Django 4.1.2 on 2022-10-06 15:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_familiar_delete_persona'),
    ]

    operations = [
        migrations.RenameField(
            model_name='familiar',
            old_name='nacimiento',
            new_name='creacion',
        ),
    ]
