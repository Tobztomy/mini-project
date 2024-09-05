# Generated by Django 4.2.13 on 2024-07-15 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_seller_customer'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='name',
            new_name='firstName',
        ),
        migrations.RenameField(
            model_name='seller',
            old_name='name',
            new_name='firstName',
        ),
        migrations.AddField(
            model_name='customer',
            name='lastName',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='seller',
            name='lastName',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
