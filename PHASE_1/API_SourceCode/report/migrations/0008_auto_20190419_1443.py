# Generated by Django 2.1.7 on 2019-04-19 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0007_auto_20190419_0733'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='img',
            field=models.URLField(blank=True, max_length=1024),
        ),
    ]
