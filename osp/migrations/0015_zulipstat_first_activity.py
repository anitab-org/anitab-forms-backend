# Generated by Django 3.0.7 on 2020-08-24 19:32

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("osp", "0014_auto_20200824_1924"),
    ]

    operations = [
        migrations.AddField(
            model_name="zulipstat",
            name="first_activity",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
