# Generated by Django 2.1.7 on 2019-03-22 00:14

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
                ('url', models.URLField(unique=True)),
                ('headline', models.CharField(default='', max_length=512)),
                ('publish', models.DateTimeField()),
                ('p_fuzz', models.CharField(choices=[('Y', 'Year'), ('M', 'Month'), ('D', 'Day'), ('H', 'Hour'), ('I', 'Minute'), ('S', 'Second'), ('A', 'Accurate')], max_length=1)),
                ('main_text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Disease',
            fields=[
                ('name', models.CharField(max_length=200, primary_key=True, serialize=False)),
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
                ('e_type', models.CharField(choices=[('P', 'Presence'), ('D', 'Death'), ('I', 'Infected'), ('H', 'Hospitalised'), ('R', 'Recovered')], max_length=1)),
                ('start_date', models.DateTimeField()),
                ('sd_fuzz', models.CharField(choices=[('Y', 'Year'), ('M', 'Month'), ('D', 'Day'), ('H', 'Hour'), ('I', 'Minute'), ('S', 'Second'), ('A', 'Accurate')], max_length=1)),
                ('end_date', models.DateTimeField()),
                ('ed_fuzz', models.CharField(choices=[('Y', 'Year'), ('M', 'Month'), ('D', 'Day'), ('H', 'Hour'), ('I', 'Minute'), ('S', 'Second'), ('A', 'Accurate')], max_length=1)),
                ('number_affected', models.IntegerField()),
                ('location', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='report.Location')),
                ('report', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='report.Report')),
            ],
        ),
        migrations.CreateModel(
            name='Syndrome',
            fields=[
                ('name', models.CharField(max_length=200, primary_key=True, serialize=False)),
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
            field=models.ManyToManyField(blank=True, to='report.Syndrome'),
        ),
    ]
