# Generated by Django 4.1.1 on 2022-09-05 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("msaref", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="total",
            name="paid",
            field=models.ManyToManyField(blank=True, to="msaref.paid"),
        ),
    ]
