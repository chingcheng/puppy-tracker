# Generated by Django 4.1.4 on 2022-12-16 00:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("records", "0005_rename_trackerlog_log"),
    ]

    operations = [
        migrations.AlterField(
            model_name="log",
            name="date",
            field=models.DateTimeField(),
        ),
    ]