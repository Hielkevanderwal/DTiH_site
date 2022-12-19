# Generated by Django 4.1.3 on 2022-12-16 11:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("pageGenerator", "0019_alter_processed_ppg_data_user_scoremodel"),
    ]

    operations = [
        migrations.AlterField(
            model_name="scoremodel",
            name="user",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
