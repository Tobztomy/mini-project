# Generated by Django 4.2.13 on 2024-07-24 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0012_remove_product_bidstartdate_product_customerid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='customerid',
        ),
        migrations.AddField(
            model_name='product',
            name='bidStartDate',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
