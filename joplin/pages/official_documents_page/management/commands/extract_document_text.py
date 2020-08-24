import urllib3
import io
import fitz
from django.core.management.base import BaseCommand, CommandError
from pages.official_documents_page.models import OfficialDocumentPage


def extract_text_from_url(url):
    # url = 'https://joplin3-austin-gov-static.s3.amazonaws.com/production/media/documents/2020-0547.pdf'
    http = urllib3.PoolManager()
    resp = http.request('GET', url)
    file_stream = io.BytesIO(resp.data)
    # Document('', < memory, doc  # 3>)
    pdf_doc = fitz.open(stream=file_stream, filetype='pdf')
    text = ''
    for page in pdf_doc:
        text += page.getText()
    return text


def extract_document_text():
    """
    """

    all_document_pages = OfficialDocumentPage.objects.all()

    url_base = 'https://joplin3-austin-gov-static.s3.amazonaws.com/production'

    for page in all_document_pages:
        '''
        get the document url
        get the data from the document url
        
        '''
        doc_url = url_base + page.document.url
        extracted_text = extract_text_from_url(doc_url)
        page.body = extracted_text
        page.save()


class Command(BaseCommand):
    help = ""

    def handle(self, *args, **options):
        extract_document_text()
