# Generated by Django 4.2.13 on 2024-07-20 05:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0010_bidtable'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bidtable',
            name='lastName',
        ),
    ]
