# Generated by Django 5.1.6 on 2025-03-04 00:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock_products', '0012_composant_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='composant',
            name='nom',
        ),
    ]
