# Generated by Django 3.0.7 on 2020-06-20 15:27

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('osp', '0003_form_question'),
    ]

    operations = [
        migrations.CreateModel(
            name='Checkbox',
            fields=[
                ('question_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='osp.Question')),
                ('options', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=255), size=None)),
            ],
            options={
                'abstract': False,
            },
            bases=('osp.question',),
        ),
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('question_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='osp.Question')),
                ('options', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=255), size=None)),
            ],
            options={
                'abstract': False,
            },
            bases=('osp.question',),
        ),
        migrations.CreateModel(
            name='Date',
            fields=[
                ('question_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='osp.Question')),
            ],
            options={
                'abstract': False,
            },
            bases=('osp.question',),
        ),
        migrations.CreateModel(
            name='Dropdown',
            fields=[
                ('question_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='osp.Question')),
                ('options', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=255), size=None)),
            ],
            options={
                'abstract': False,
            },
            bases=('osp.question',),
        ),
        migrations.CreateModel(
            name='FileUpload',
            fields=[
                ('question_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='osp.Question')),
            ],
            options={
                'abstract': False,
            },
            bases=('osp.question',),
        ),
        migrations.CreateModel(
            name='Paragraph',
            fields=[
                ('question_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='osp.Question')),
            ],
            options={
                'abstract': False,
            },
            bases=('osp.question',),
        ),
        migrations.CreateModel(
            name='ShortAnswer',
            fields=[
                ('question_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='osp.Question')),
            ],
            options={
                'abstract': False,
            },
            bases=('osp.question',),
        ),
        migrations.CreateModel(
            name='Time',
            fields=[
                ('question_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='osp.Question')),
            ],
            options={
                'abstract': False,
            },
            bases=('osp.question',),
        ),
    ]