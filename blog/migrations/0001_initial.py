# Generated by Django 5.0.1 on 2024-01-29 13:33

import django.db.models.deletion
import wagtailmarkdown.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0089_log_entry_data_json_null_to_object'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('blog_title', models.TextField(blank=True)),
                ('blog_slug', models.SlugField(blank=True, unique=True)),
                ('blog_body', wagtailmarkdown.fields.MarkdownField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]
