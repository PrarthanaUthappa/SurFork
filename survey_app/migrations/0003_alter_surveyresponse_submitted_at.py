# Generated by Django 5.0.6 on 2025-03-06 09:19

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey_app', '0002_rename_approved_surveyresponse_is_approved'),
    ]

    operations = [
        migrations.AlterField(
            model_name='surveyresponse',
            name='submitted_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
