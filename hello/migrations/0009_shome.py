# Generated by Django 4.1.2 on 2023-02-07 02:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("hello", "0008_alter_userinfo_email"),
    ]

    operations = [
        migrations.CreateModel(
            name="Shome",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("hometype", models.CharField(blank=True, max_length=4, null=True)),
                (
                    "price",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=100, null=True
                    ),
                ),
                ("addy", models.CharField(blank=True, max_length=4, null=True)),
                (
                    "size",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=100, null=True
                    ),
                ),
                (
                    "beds",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=100, null=True
                    ),
                ),
                (
                    "bath",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=100, null=True
                    ),
                ),
            ],
        ),
    ]
