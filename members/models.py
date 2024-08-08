from django.db import models
from wagtail.fields import RichTextField
from wagtail.api import APIField
from wagtail.models import Page
from wagtail.admin.panels import FieldPanel
from wagtailmarkdown.fields import MarkdownField

class MembersPage(Page):
    name = models.CharField(max_length=100, null=True)
    batch = models.IntegerField(null=True)
    members_slug = models.IntegerField(null=True)
    content_panels = Page.content_panels + [
        FieldPanel('name'),
        FieldPanel('batch'),
        FieldPanel('members_slug')
    ]
    api_fields = [
        APIField('name'),
        APIField('batch'),
        APIField('members_slug')
    ]
    def __str__(self):
            return self.name