# Generated by Django 2.1.7 on 2019-03-21 21:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reportevent',
            old_name='number_effecet',
            new_name='number_effect',
        ),
    ]
