# Generated by Django 4.1.1 on 2022-09-05 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("msaref", "0002_total_paid"),
    ]

    operations = [
        migrations.AddField(
            model_name="paid",
            name="done",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="paid",
            name="paid_up",
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name="paid",
            name="residual",
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
