# Generated by Django 4.1.5 on 2023-01-11 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0004_remove_order_tags_product_tags"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="description",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
