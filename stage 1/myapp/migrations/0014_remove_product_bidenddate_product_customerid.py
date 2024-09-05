# Generated by Django 4.2.13 on 2024-07-24 12:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0013_remove_product_customerid_product_bidstartdate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='bidEndDate',
        ),
        migrations.AddField(
            model_name='product',
            name='customerid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.customer'),
        ),
    ]
