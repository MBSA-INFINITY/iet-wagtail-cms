# Generated by Django 5.0.1 on 2024-01-29 13:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpage',
            name='published_on',
            field=models.DateField(blank=True, default=datetime.date(2024, 1, 29), null=True),
        ),
    ]
