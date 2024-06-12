# Generated by Django 5.0.6 on 2024-06-07 01:21

import django.utils.timezone
import django_countries.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ApplicantForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=100)),
                ('surname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female')], default='male', max_length=10)),
                ('Date_of_birth', models.DateTimeField(default=django.utils.timezone.now)),
                ('cls', models.CharField(max_length=10)),
                ('phone_number', models.IntegerField()),
                ('Email_Address', models.EmailField(max_length=254)),
                ('passport', models.ImageField(upload_to='')),
                ('birth_certificate', models.ImageField(upload_to='')),
                ('country', django_countries.fields.CountryField(blank=True, max_length=2)),
                ('state', models.CharField(max_length=100)),
                ('Address', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ParentForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Fathername', models.CharField(max_length=250)),
                ('Mothername', models.CharField(max_length=250)),
                ('F_phone', models.IntegerField()),
                ('M_phone', models.IntegerField()),
                ('F_occupition', models.CharField(max_length=15)),
                ('M_occupition', models.CharField(max_length=15)),
            ],
        ),
    ]
