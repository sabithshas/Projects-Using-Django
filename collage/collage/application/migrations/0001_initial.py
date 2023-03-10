# Generated by Django 4.1.3 on 2023-01-16 09:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="leave",
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
                ("date", models.DateField(max_length=10)),
                ("reason", models.CharField(max_length=70)),
                ("status", models.CharField(max_length=10)),
                ("role", models.CharField(max_length=10)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Add_teacher",
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
                ("Hfirstname", models.CharField(max_length=30)),
                ("Hlastname", models.CharField(max_length=30)),
                ("Husername", models.CharField(max_length=20)),
                ("Hadress", models.CharField(max_length=50)),
                ("Hplace", models.CharField(max_length=30)),
                ("Hphone", models.IntegerField()),
                ("Hemail", models.EmailField(max_length=254)),
                ("Hdepartment", models.CharField(max_length=15)),
                ("Hsubject", models.CharField(max_length=15)),
                ("Hqualification", models.CharField(max_length=30)),
                ("Hexperience", models.CharField(max_length=50)),
                ("Hpassword", models.CharField(max_length=15)),
                ("Hcpassword", models.CharField(max_length=15)),
                ("role", models.CharField(max_length=10)),
                ("status", models.CharField(max_length=30)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Add_students",
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
                ("Sfirstname", models.CharField(max_length=30)),
                ("Slastname", models.CharField(max_length=30)),
                ("Susername", models.CharField(max_length=20)),
                ("Sadress", models.CharField(max_length=50)),
                ("Splace", models.CharField(max_length=30)),
                ("Sphone", models.IntegerField()),
                ("Semail", models.EmailField(max_length=254)),
                ("Sdepartment", models.CharField(max_length=15)),
                ("Ssubject", models.CharField(max_length=15)),
                ("SAdmission", models.IntegerField()),
                ("Spassword", models.CharField(max_length=15)),
                ("Scpassword", models.CharField(max_length=15)),
                ("Srole", models.CharField(max_length=10)),
                ("Sstatus", models.CharField(max_length=30)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Add_hod",
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
                ("Firstname", models.CharField(max_length=30)),
                ("Lastname", models.CharField(max_length=30)),
                ("username", models.CharField(max_length=20)),
                ("Address", models.CharField(max_length=20)),
                ("place", models.CharField(max_length=20)),
                ("phone", models.IntegerField()),
                ("email", models.EmailField(max_length=254)),
                ("Department", models.CharField(max_length=15)),
                ("qualification", models.CharField(max_length=15)),
                ("experience", models.CharField(max_length=100)),
                ("password", models.CharField(max_length=15)),
                ("confirmpassword", models.CharField(max_length=15)),
                ("role", models.CharField(max_length=10)),
                ("status", models.CharField(max_length=30)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
