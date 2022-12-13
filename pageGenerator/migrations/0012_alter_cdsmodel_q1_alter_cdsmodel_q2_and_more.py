# Generated by Django 4.1.3 on 2022-12-12 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("pageGenerator", "0011_alter_cdsmodel_q1_alter_cdsmodel_q10_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="cdsmodel",
            name="q1",
            field=models.IntegerField(
                verbose_name="Please rate your cigarette addiction on a scale from 0 to 100 with 0 being not addicted and 100 being extremely addicted."
            ),
        ),
        migrations.AlterField(
            model_name="cdsmodel",
            name="q2",
            field=models.IntegerField(
                verbose_name="On average, how many cigarettes do you smoke per day?"
            ),
        ),
        migrations.AlterField(
            model_name="cdsmodel",
            name="q3",
            field=models.IntegerField(
                verbose_name="How soon after waking up do you smoke your first cigarette?"
            ),
        ),
    ]
