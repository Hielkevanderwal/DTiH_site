# Generated by Django 4.1.3 on 2023-01-09 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "pageGenerator",
            "0002_remove_raw_ppg_data_user_delete_processed_ppg_data_and_more",
        ),
    ]

    operations = [
        migrations.AddField(
            model_name="accesto", name="BMI", field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name="accesto", name="ADS", field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name="accesto", name="CDS", field=models.BooleanField(default=True),
        ),
    ]
