# Generated by Django 4.2.13 on 2024-07-17 04:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_feedback'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=300)),
                ('date', models.DateField(auto_now=True)),
                ('time', models.CharField(max_length=100)),
                ('utype', models.CharField(max_length=100)),
                ('customerid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.customer')),
                ('sellerid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.seller')),
            ],
        ),
    ]
