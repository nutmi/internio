# Generated by Django 4.1.11 on 2023-10-17 02:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Scraper", "0009_alter_joblistings_apply_link_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="joblistings",
            name="apply_link",
            field=models.URLField(blank=True, default="", max_length=500, null=True),
        ),
    ]