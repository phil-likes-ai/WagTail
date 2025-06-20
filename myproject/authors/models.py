from django.db import models
from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel
# from wagtail.images.edit_handlers import ImageChooserPanel # Pre-Wagtail 5
# from wagtail.images.widgets import ImageChooser # For Wagtail 5+ in FieldPanel, not directly used in panels

# For Wagtail 5 and above, ImageChooserPanel is replaced by using FieldPanel with ImageChooser widget
# from wagtail.images.edit_handlers import ImageChooserPanel # Older Wagtail
# If using Wagtail < 5, uncomment the above and use ImageChooserPanel('profile_picture')

class AuthorPage(Page):
    # name = models.CharField(max_length=255) # Using title from Page model for author's name
    bio = RichTextField(blank=True)
    profile_picture = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    content_panels = Page.content_panels + [
        # FieldPanel('name'), # If using a separate name field
        FieldPanel('bio'),
        FieldPanel('profile_picture'), # For Wagtail 5+, this will automatically use the correct widget
                                      # For older Wagtail, use ImageChooserPanel('profile_picture')
    ]

    # parent_page_types = ['authors.AuthorIndexPage'] # Assuming an AuthorIndexPage
    # subpage_types = []
