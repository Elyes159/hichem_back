# Generated by Django 5.1.6 on 2025-02-24 00:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Auth', '0005_superadmin_is_blocked'),
    ]

    operations = [
        migrations.AlterField(
            model_name='superadmin',
            name='is_blocked',
            field=models.BooleanField(default=False, editable=False),
        ),
    ]
