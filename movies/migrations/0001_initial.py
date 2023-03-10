# Generated by Django 4.1.6 on 2023-02-16 01:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('foundation_date', models.DateField(null=True)),
                ('continent', models.CharField(blank=True, max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('surname', models.CharField(max_length=20)),
                ('birthday', models.DateField(null=True)),
                ('country', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='movies.country')),
            ],
        ),
        migrations.CreateModel(
            name='ProductionCompany',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('foundation_date', models.DateField(null=True)),
                ('country_of_origin', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='movies.country')),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('genre', models.CharField(max_length=20)),
                ('score', models.DecimalField(decimal_places=2, max_digits=3, null=True)),
                ('age_restricted', models.BooleanField(null=True)),
                ('director', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='movies.director')),
                ('production_company', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='movies.productioncompany')),
            ],
        ),
    ]
