from django.db import models
from wagtail.fields import RichTextField
from wagtail.api import APIField
from wagtail.models import Page
from wagtail.admin.panels import FieldPanel
from wagtailmarkdown.fields import MarkdownField
from datetime import date

class EventsPage(Page):
    event_title = RichTextField(blank=True)
    event_slug = models.SlugField(unique = True, blank=True)
    event_date = models.DateField(null = True, blank = True, default=date.today())
    event_organizer = models.TextField(null = True, blank = True)
    event_location = models.TextField(null = True, blank = True)
    event_img_url = models.URLField(blank=False, null=True)
    event_tags= models.TextField(blank=True)
    event_body = MarkdownField(blank=True, null=True)

    content_panels = Page.content_panels + [
        FieldPanel('event_title'),
        FieldPanel('event_slug'),
        FieldPanel('event_date'),
        FieldPanel('event_organizer'),
        FieldPanel('event_location'),
        FieldPanel('event_tags'),
        FieldPanel('event_img_url'),
        FieldPanel('event_body', classname="full"),
    ]
    api_fields = [
        APIField('event_title'),
        APIField('event_slug'),
        APIField('event_date'),
        APIField('event_organizer'),
        APIField('event_location'),
        APIField('event_tags'),
        APIField('event_img_url'),
        APIField('event_body'),
    ]
