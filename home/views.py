from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import logging

logger = logging.getLogger(__name__)

# Create your views here.
# <meta name="wa4e" content="d2ddea18f00665ce8623e36bd4e3c7c5">

def index(request):
    logging.error('Hello world DJ4E in the log...')
    print('Hello world DJ4E in a print statement...')
    response = """<html><body><p>Hello world DJ4E in HTML</p>
    <p> I love cats! My kitten/daughter-in-law is named Phoenix</p>
    </body></html>"""
    return HttpResponse(response)
