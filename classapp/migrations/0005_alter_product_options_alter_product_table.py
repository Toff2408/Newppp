# Generated by Django 4.1.2 on 2022-10-24 15:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('classapp', '0004_alter_category_options_alter_product_p_discount_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'managed': True, 'verbose_name': 'Product', 'verbose_name_plural': 'Products'},
        ),
        migrations.AlterModelTable(
            name='product',
            table='Product',
        ),
    ]
