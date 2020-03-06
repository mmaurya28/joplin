from django.db import models

from wagtail.core.models import Page

from .translated_image import TranslatedImage


class HomePage(Page):
    parent_page_types = []
    # subpage_types = ['base.ServicePage', 'base.ProcessPage', 'base.InformationPage', 'base.DepartmentPage']
    subpage_types = [
        'service_page.ServicePage',
        'information_page.InformationPage',
        'department_page.DepartmentPage',
        'topic_page.TopicPage',
        'location_page.LocationPage',
        'event_page.EventPage'
    ]

    image = models.ForeignKey(TranslatedImage, null=True, on_delete=models.SET_NULL, related_name='+')
