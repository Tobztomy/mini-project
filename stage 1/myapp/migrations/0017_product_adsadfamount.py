# Generated by Django 4.2.13 on 2024-07-25 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0016_remove_product_ssssss'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='adsadfamount',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
