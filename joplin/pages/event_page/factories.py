import factory
from pages.base_page.factories import JanisBasePageFactory
from pages.home_page.models import HomePage
from pages.event_page.models import EventPage

class EventPageFactory(JanisBasePageFactory):
    class Meta:
        model = EventPage

def create_event_page_from_importer_dictionaries(page_dictionaries, revision_id):
    # first check to see if we already imported this page
    # if we did, just go to the edit page for it without changing the db
    # todo: maybe change this to allow updating pages in the future?
    try:
        page = EventPage.objects.get(imported_revision_id=revision_id)
    except EventPage.DoesNotExist:
        page = None
    if page:
        return page

    # since we don't have a page matching the revision id, we should look
    # for other matches, for now let's just use english slug
    # todo: figure out what we want the logic around importing a page with the same slug to look like
    try:
        page = EventPage.objects.get(slug=page_dictionaries['en']['slug'])
    except EventPage.DoesNotExist:
        page = None
    if page:
        return page

    # since we don't have a page matching the revision id or the slug
    # make the combined page dictionary
    combined_dictionary = page_dictionaries['en']

    # todo: contacts
    # remove contacts if we have it because:
    # * it might be what's wrong rn
    # todo: why isn't pop working?
    # if 'contacts' in combined_dictionary:
    #     del combined_dictionary['contacts']


    # Set home as parent
    combined_dictionary['parent'] = HomePage.objects.first()

    # set the translated fields
    for field in EventPageFactory._meta.model._meta.fields:
        if field.column.endswith("_es"):
            if field.column[:-3] in page_dictionaries['es']:
                combined_dictionary[field.column] = page_dictionaries['es'][field.column[:-3]]

    # todo: actually get departments here
    # combined_dictionary['add_department'] = ['just a string']

    page = EventPageFactory.create(**combined_dictionary)
    return page
