# Generated by Django 5.1.4 on 2025-01-14 13:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("outflows", "0002_alter_outflow_id"),
    ]

    operations = [
        migrations.RenameField(
            model_name="outflow",
            old_name="implementd",
            new_name="implemented",
        ),
    ]
