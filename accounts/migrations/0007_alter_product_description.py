# Generated by Django 4.1.7 on 2023-03-08 02:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0006_remove_order_tags_product_tags"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="description",
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
