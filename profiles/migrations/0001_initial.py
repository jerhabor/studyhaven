# Generated by Django 3.2 on 2021-04-24 17:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('default_full_name', models.CharField(blank=True, max_length=50)),
                ('default_email_address', models.EmailField(blank=True, max_length=254)),
                ('default_phone_number', models.CharField(blank=True, max_length=20)),
                ('default_country', django_countries.fields.CountryField(blank=True, max_length=2, null=True)),
                ('default_address_line1', models.CharField(blank=True, max_length=90)),
                ('default_address_line2', models.CharField(blank=True, max_length=90)),
                ('default_city_or_town', models.CharField(blank=True, max_length=50)),
                ('default_postcode', models.CharField(blank=True, max_length=10)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
