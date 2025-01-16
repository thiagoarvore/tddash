# Generated by Django 5.1.4 on 2025-01-16 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "implementations",
            "0002_implementation_billing_date_implementation_cnpj_and_more",
        ),
    ]

    operations = [
        migrations.AddField(
            model_name="implementation",
            name="solution",
            field=models.CharField(
                choices=[("Zoox Wi-fi", "Zoox Wi-fi"), ("Propz", "Propz")],
                default="Zoox Wi-Fi",
                max_length=40,
            ),
        ),
    ]
