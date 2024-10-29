# Generated by Django 3.2.18 on 2023-03-24 11:16

from django.db import migrations
import stdimage.models


class Migration(migrations.Migration):
    dependencies = [
        ("nuntius", "0023_add_help_text_to_pushcampaign_notification_tag"),
    ]

    operations = [
        migrations.AlterField(
            model_name="mosaicoimage",
            name="file",
            field=stdimage.models.StdImageField(
                force_min_size=False,
                upload_to="mosaico",
                variations={"thumbnail": (90, 90)},
            ),
        ),
    ]
