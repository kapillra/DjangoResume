# Generated by Django 5.0.6 on 2024-07-12 03:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("resumeApp", "0004_project_company"),
    ]

    operations = [
        migrations.AddField(
            model_name="userprofile",
            name="ProfileImage",
            field=models.FileField(default="avatar.png", upload_to="profile_images/"),
        ),
    ]
