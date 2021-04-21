# Generated by Django 3.2 on 2021-04-21 14:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0002_alter_category_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_number', models.CharField(editable=False, max_length=32)),
                ('full_name', models.CharField(max_length=50)),
                ('email_address', models.EmailField(max_length=254)),
                ('phone_number', models.EmailField(max_length=20)),
                ('country', models.EmailField(max_length=40)),
                ('address_line1', models.CharField(max_length=90)),
                ('address_line2', models.CharField(max_length=90)),
                ('city_or_town', models.CharField(max_length=50)),
                ('postcode', models.CharField(blank=True, max_length=10)),
                ('order_date', models.DateTimeField(auto_now_add=True)),
                ('order_total', models.DecimalField(decimal_places=2, default=0, max_digits=8)),
                ('delivery', models.DecimalField(decimal_places=2, default=0, max_digits=4)),
                ('grand_total', models.DecimalField(decimal_places=2, default=0, max_digits=8)),
            ],
        ),
        migrations.CreateModel(
            name='eachProductOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=0)),
                ('product_order_total', models.DecimalField(decimal_places=2, editable=False, max_digits=6)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='each_product', to='checkout.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
            ],
        ),
    ]