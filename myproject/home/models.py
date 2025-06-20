from django.db import models

from wagtail.models import Page


class HomePage(Page):
    pass


class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()
