# Generated by Django 4.1.4 on 2022-12-15 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("records", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="record",
            name="date",
            field=models.DateField(null=True),
        ),
    ]
