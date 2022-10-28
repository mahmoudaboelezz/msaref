# Generated by Django 4.1.1 on 2022-09-06 13:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("msaref", "0007_rename_band_paid_band_elm_band_paid_elm"),
    ]

    operations = [
        migrations.AddField(
            model_name="paid",
            name="by",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]