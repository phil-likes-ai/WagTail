from django.db import models
from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel # , MultiFieldPanel, InlinePanel

# from wagtail.search import index # If making it searchable

class ArticlePage(Page):
    publication_date = models.DateField("Post date")
    body = RichTextField(blank=True)
    author = models.ForeignKey(
        'authors.AuthorPage', # App name and model name
        null=True,
        blank=True, # Decide if an article MUST have an author
        on_delete=models.SET_NULL,
        related_name='articles_by_author', # Optional: useful for reverse lookups
    )

    content_panels = Page.content_panels + [
        FieldPanel('publication_date'),
        FieldPanel('body'),
        FieldPanel('author'), # Add when AuthorPage is defined
    ]

    # Optional: specify parent page types
    # parent_page_types = ['news.NewsIndexPage'] # Assuming a NewsIndexPage
    # Optional: specify subpage types
    # subpage_types = []
