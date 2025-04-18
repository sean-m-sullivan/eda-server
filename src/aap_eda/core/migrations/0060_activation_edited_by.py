# Generated by Django 4.2.16 on 2025-03-10 16:32

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0059_alter_activation_user_alter_eventstream_owner"),
    ]

    operations = [
        migrations.AddField(
            model_name="activation",
            name="edited_by",
            field=models.ForeignKey(
                default=None,
                editable=False,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="%s(class)s_edited+",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
