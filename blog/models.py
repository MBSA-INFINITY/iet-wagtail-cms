from django.db import models
from wagtail.fields import RichTextField
from wagtail.api import APIField
from wagtail.models import Page
from wagtail.admin.panels import FieldPanel
from wagtailmarkdown.fields import MarkdownField
from datetime import date

class BlogPage(Page):
    blog_title = models.TextField(blank=True)
    blog_slug = models.SlugField(unique = True, blank=True)
    blog_description= MarkdownField(blank=False, null=True)
    blog_authors= models.TextField(blank=True)
    blog_tags= models.TextField(blank=True)
    published_on = models.DateField(null = True, blank = True, default=date.today())
    blog_body = MarkdownField(blank=True, null=True)
    blog_img_url = models.URLField(blank=False, null=True)

    content_panels = Page.content_panels + [
        FieldPanel('blog_title'),
        FieldPanel('blog_slug'),
        FieldPanel('blog_authors'),
        FieldPanel('blog_img_url'),
        FieldPanel('blog_description'),
        FieldPanel('published_on'),
        FieldPanel('blog_tags'),
        FieldPanel('blog_body', classname="full")
    ]
    api_fields = [
        APIField('blog_body'),
        APIField('blog_img_url'),
        APIField('blog_title'),
        APIField('blog_authors'),
        APIField('published_on'),
        APIField('blog_slug'),
        APIField('blog_description'),
        APIField('blog_tags')
    ]
