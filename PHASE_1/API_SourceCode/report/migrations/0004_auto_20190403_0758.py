# Generated by Django 2.1.7 on 2019-04-03 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0003_auto_20190329_0710'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reportevent',
            name='number_affected',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
