# Generated by Django 2.1.7 on 2019-03-05 10:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
                ('headline', models.CharField(default='', max_length=512)),
                ('publish', models.DateTimeField()),
                ('p_fuzz', models.DateTimeField(choices=[('M', 'Month'), ('D', 'Day'), ('H', 'Hour'), ('I', 'Minute'), ('S', 'Second')], max_length=1)),
                ('main_text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Disease',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=512)),
                ('lat', models.DecimalField(decimal_places=20, max_digits=24)),
                ('lng', models.DecimalField(decimal_places=20, max_digits=24)),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(blank=True)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='report.Article')),
                ('disease', models.ManyToManyField(blank=True, to='report.Disease')),
            ],
        ),
        migrations.CreateModel(
            name='ReportEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('report_type', models.CharField(max_length=200)),
                ('start_date', models.DateTimeField()),
                ('sd_fuzz', models.CharField(choices=[('M', 'Month'), ('D', 'Day'), ('H', 'Hour'), ('I', 'Minute'), ('S', 'Second')], max_length=1)),
                ('end_date', models.DateTimeField()),
                ('ed_fuzz', models.CharField(choices=[('M', 'Month'), ('D', 'Day'), ('H', 'Hour'), ('I', 'Minute'), ('S', 'Second')], max_length=1)),
                ('number_effecet', models.IntegerField(blank=True, null=True)),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='report.Location')),
                ('report', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='report.Report')),
            ],
        ),
        migrations.CreateModel(
            name='Syndrome',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='report',
            name='syndrome',
            field=models.ManyToManyField(blank=True, to='report.Syndrome'),
        ),
        migrations.AddField(
            model_name='disease',
            name='syndromes',
            field=models.ManyToManyField(blank=True, null=True, to='report.Syndrome'),
        ),
    ]
