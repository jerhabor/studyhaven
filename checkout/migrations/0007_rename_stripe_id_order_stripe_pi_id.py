# Generated by Django 3.2 on 2021-04-24 00:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0006_auto_20210424_0029'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='stripe_id',
            new_name='stripe_pi_id',
        ),
    ]
