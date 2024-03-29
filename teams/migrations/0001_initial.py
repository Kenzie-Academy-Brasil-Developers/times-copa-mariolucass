# Generated by Django 4.1.6 on 2023-02-04 12:50

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Team",
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
                ("name", models.CharField(max_length=30)),
                ("titles", models.CharField(default=0, max_length=50)),
                ("top_scorer", models.CharField(max_length=50)),
                ("fifa_code", models.CharField(max_length=3, unique=True)),
                ("first_cup", models.DateField(max_length=50, null=True)),
            ],
        ),
    ]
