from django.db import models
from members.models import MembersPage
from wagtail.fields import RichTextField
from wagtail.api import APIField
from wagtail.models import Page
from wagtail.admin.panels import FieldPanel
from wagtailmarkdown.fields import MarkdownField
from datetime import date
# from dal import autocomplete

class ProjectsPage(Page):

    project_title = models.TextField(blank=False, null=True)
    project_sig= models.TextField(blank=False, 
                                  null=True)
    project_slug = models.SlugField(unique = True, blank=True)
    project_year = models.IntegerField(blank=True)
    project_description= MarkdownField(blank=False, null=True)
    project_tags= models.TextField(blank=True)
    project_authors= models.TextField(blank=True)
    github_url = models.URLField(blank=False, null=True)
    project_body = MarkdownField(blank=True, null=True)
    project_img_url = models.URLField(blank=False, null=True)
    # authors = models.ManyToManyField('Author', related_name='blog_posts', widget=autocomplete.SelectMultiple(url='author-autocomplete'))

    content_panels = Page.content_panels + [
        FieldPanel('project_title'),
        FieldPanel('project_sig'),
        FieldPanel('project_slug'),
        FieldPanel('project_year'),
        FieldPanel('project_authors'),
        FieldPanel('github_url'),
        FieldPanel('project_img_url'),
        FieldPanel('project_description'),
        FieldPanel('project_tags'),
        FieldPanel('project_body', classname="full"),
    ]
    api_fields = [
        APIField('project_title'),
        APIField('project_sig'),
        APIField('project_slug'),
        APIField('project_year'),
        APIField('project_authors'),
        APIField('github_url'),
        APIField('project_img_url'),
        APIField('project_description'),
        APIField('project_tags'),
        APIField('project_body'),
    ]
