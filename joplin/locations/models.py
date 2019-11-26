from django.db import models
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.images.models import Image
from wagtail.images.edit_handlers import ImageChooserPanel
from phonenumber_field.modelfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberInternationalFallbackWidget
from base.models import JanisBasePage, HomePage
from wagtail.core.models import Page, Orderable
from modelcluster.fields import ParentalKey
from wagtail.admin.edit_handlers import (
    FieldPanel,
    InlinePanel,
    MultiFieldPanel,
    ObjectList,
    TabbedInterface,
    FieldRowPanel,
    StreamFieldPanel,
)
from base.models.translated_image import TranslatedImage
from base.models import Location as BaseLocation

# The abstract model for related links, complete with panels
from wagtail.core.fields import RichTextField, StreamField
from wagtail.search import index
from wagtail.admin.edit_handlers import FieldPanel, PageChooserPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from base.models import JanisBasePage
from base.models.widgets import countMe, countMeTextArea, AUTHOR_LIMITS
from modelcluster.models import ClusterableModel
from base.models.constants import DEFAULT_MAX_LENGTH
from base.models.day_and_duration import DayAndDuration
from wagtail.snippets.edit_handlers import SnippetChooserPanel

from wagtail.core import blocks


class LocationPage(JanisBasePage):
    """
    all the relevant details for a specifc location (place!?)
    decide if we want to set null or cascade
    """
    janis_url_page_type = 'location'
    alternate_name = models.CharField(max_length=255, blank=True)

    physical_street = models.CharField(max_length=255, blank=True)
    physical_unit = models.CharField(max_length=255, blank=True)
    physical_city = models.CharField(max_length=255, default='Austin', blank=True)
    physical_state = models.CharField(max_length=255, default='TX', blank=True)
    physical_country = models.CharField(max_length=255, default='USA', blank=True)
    physical_zip = models.CharField(max_length=255, blank=True)

    physical_location_photo = models.ForeignKey(
        TranslatedImage,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    phone_description = models.CharField(
        max_length=DEFAULT_MAX_LENGTH, blank=True)
    phone_number = PhoneNumberField(blank=True)
    email = models.EmailField(blank=True)

    mailing_street = models.CharField(max_length=255, blank=True)
    mailing_city = models.CharField(max_length=255, default='Austin', blank=True)
    mailing_state = models.CharField(max_length=255, default='TX', blank=True)
    mailing_country = models.CharField(max_length=255, default='USA', blank=True)
    mailing_zip = models.CharField(max_length=255, blank=True)

    nearest_bus_1 = models.IntegerField(blank=True)
    nearest_bus_2 = models.IntegerField(blank=True)
    nearest_bus_3 = models.IntegerField(blank=True)

    parent_page_types = ['base.HomePage', 'LocationsIndexPage']

    content_panels = [
        FieldPanel('title_en', widget=countMe),

        MultiFieldPanel(children=[
            FieldPanel('physical_street'),
            FieldPanel('physical_unit', classname='col2'),
            FieldPanel('physical_city', classname='col5'),
            FieldPanel('physical_state', classname='col4'),
            FieldPanel('physical_zip', classname='col2'),
            FieldPanel('physical_country', classname='col5'),
        ], heading='Physical Address'),
        ImageChooserPanel('physical_location_photo'),
        MultiFieldPanel(children=[
            FieldPanel('mailing_street'),
            FieldPanel('mailing_city', classname='col5'),
            FieldPanel('mailing_state', classname='col4'),
            FieldPanel('mailing_zip', classname='col2'),
            FieldPanel('mailing_country', classname='col5'),
        ],
            heading='Mailing Address',
            classname="collapsible"
        ),
        FieldPanel('alternate_name'),
        FieldRowPanel(
            children=[
                FieldPanel('phone_number', classname='col6',
                           widget=PhoneNumberInternationalFallbackWidget),
                FieldPanel('phone_description', classname='col6'),
                FieldPanel('email', classname='col6'),
            ],
            heading="Location phone"
        ),


        FieldRowPanel(
            children=[
                FieldPanel('nearest_bus_1'),
                FieldPanel('nearest_bus_2'),
                FieldPanel('nearest_bus_3'),
            ],
            heading="Nearest bus"
        ),
        InlinePanel('related_services', label='Related Services'),
    ]


class LocationPageRelatedServices(ClusterableModel):

    page = ParentalKey(LocationPage, related_name='related_services', default=None)
    related_service = models.ForeignKey(
        "base.servicePage",
        on_delete=models.PROTECT,
    )
    panels = [
        PageChooserPanel("related_service"),

    ]


"""
here we want to add these fields to this model, but typing them all out would be super verbose
so a little python and Django's contribute_to_class go a long way
"""


def add_hours_by_day_and_exceptions(model):
    week_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    panels_to_add = []
    models.TextField(max_length=255, blank=True).contribute_to_class(model, 'hours_exceptions')
    for day in week_days:
        day_start_field = '%s_start_time' % day.lower()
        day_end_field = '%s_end_time' % day.lower()
        day_open_field = '%s_open' % day.lower()
        models.BooleanField(default=False).contribute_to_class(model, day_open_field)
        models.TimeField(null=True, blank=True).contribute_to_class(model, day_start_field)
        models.TimeField(null=True, blank=True).contribute_to_class(model, day_end_field)
        models.TimeField(null=True, blank=True).contribute_to_class(model, day_start_field + "_2")
        models.TimeField(null=True, blank=True).contribute_to_class(model, day_end_field + "_2")
        panels_to_add += [

            FieldRowPanel(
                children=[

                    FieldPanel(day_start_field),
                    FieldPanel(day_end_field),
                    FieldPanel(day_start_field + "_2"),
                    FieldPanel(day_end_field + "_2"),
                ],
                heading="Hours",
            ),

        ]
    panels_to_add += [
        FieldPanel('hours_exceptions')
    ]
    panels_with_wrapper = MultiFieldPanel(children=panels_to_add, classname="collapsible", heading="Location Hours")
    return panels_with_wrapper


LocationPageRelatedServices.panels += [add_hours_by_day_and_exceptions(LocationPageRelatedServices)]

LocationPage.content_panels += [add_hours_by_day_and_exceptions(LocationPage)]


class LocationsIndexPage(Page):
    """
    A list of LocationPages
    """

    # Overrides the context to list all child
    # items, that are live, by the date that they were published
    # http://docs.wagtail.io/en/latest/getting_started/tutorial.html#overriding-context
    def get_context(self, request):
        context = super(LocationsIndexPage, self).get_context(request)
        context['locations'] = LocationPage.objects.descendant_of(
            self).live().order_by(
            'primary_name')
        return context


"""
maybe try this~! https://gist.github.com/pjho/f0bbcfc745989191cf305a34233388e0
"""
