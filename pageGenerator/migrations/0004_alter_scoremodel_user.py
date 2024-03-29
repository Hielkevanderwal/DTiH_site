# Generated by Django 4.1.3 on 2023-01-09 12:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("pageGenerator", "0003_accesto_bmi_alter_accesto_ads_alter_accesto_cds"),
    ]

    operations = [
        migrations.AlterField(
            model_name="scoremodel",
            name="user",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="ScoreModel",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
