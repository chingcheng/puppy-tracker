# Generated by Django 4.1.4 on 2022-12-17 01:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("records", "0011_alter_log_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="log",
            name="date",
            field=models.DateField(),
        ),
    ]