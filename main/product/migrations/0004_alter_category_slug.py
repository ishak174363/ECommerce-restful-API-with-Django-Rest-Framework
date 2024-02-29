# Generated by Django 5.0.2 on 2024-02-29 13:57

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("product", "0003_category_is_active_category_slug"),
    ]

    operations = [
        migrations.AlterField(
            model_name="category",
            name="slug",
            field=autoslug.fields.AutoSlugField(
                editable=False, max_length=250, populate_from="name", unique=True
            ),
        ),
    ]