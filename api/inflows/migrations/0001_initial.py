# Generated by Django 5.1.4 on 2025-01-14 13:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("products", "0001_initial"),
        ("suppliers", "0002_alter_supplier_name"),
    ]

    operations = [
        migrations.CreateModel(
            name="Inflow",
            fields=[
                ("id", models.UUIDField(primary_key=True, serialize=False)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("quantity", models.PositiveSmallIntegerField()),
                ("cost_price", models.DecimalField(decimal_places=2, max_digits=20)),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="inflows",
                        to="products.product",
                    ),
                ),
                (
                    "supplier",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="inflows",
                        to="suppliers.supplier",
                    ),
                ),
            ],
            options={
                "ordering": ["product"],
            },
        ),
    ]
