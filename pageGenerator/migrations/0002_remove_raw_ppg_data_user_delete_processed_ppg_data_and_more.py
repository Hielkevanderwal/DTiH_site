# Generated by Django 4.1.3 on 2022-12-22 13:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("pageGenerator", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(model_name="raw_ppg_data", name="user",),
        migrations.DeleteModel(name="Processed_ppg_data",),
        migrations.DeleteModel(name="Raw_ppg_data",),
    ]
