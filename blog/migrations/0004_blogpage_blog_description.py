# Generated by Django 4.2.4 on 2024-02-22 12:55

from django.db import migrations
import wagtailmarkdown.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_blogpage_published_on'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpage',
            name='blog_description',
            field=wagtailmarkdown.fields.MarkdownField(null=True),
        ),
    ]
