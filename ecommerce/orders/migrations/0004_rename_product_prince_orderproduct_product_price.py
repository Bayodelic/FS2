# Generated by Django 5.0.6 on 2024-06-11 07:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_rename_oayment_orderproduct_payment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderproduct',
            old_name='product_prince',
            new_name='product_price',
        ),
    ]
