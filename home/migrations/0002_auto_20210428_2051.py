# Generated by Django 3.2 on 2021-04-28 20:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Reviews',
            new_name='Review',
        ),
        migrations.AlterModelOptions(
            name='review',
            options={},
        ),
    ]
