from webapp.forms import SimpleSearchForm
from django.urls import translate_url
from django.conf import settings


def search_form(request):
    form = SimpleSearchForm(request.GET)
    return {'search_form': form}


def strip_language_code(request):
    return {
        'default_language': settings.LANGUAGE_CODE,
        'language_base_link': translate_url(request.path, settings.LANGUAGE_CODE)
    }
