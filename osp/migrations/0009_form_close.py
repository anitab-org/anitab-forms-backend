# Generated by Django 3.0.7 on 2020-07-12 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('osp', '0008_auto_20200708_1817'),
    ]

    operations = [
        migrations.AddField(
            model_name='form',
            name='close',
            field=models.BooleanField(default=False),
        ),
    ]
