from fluent.runtime import FluentLocalization, FluentResourceLoader
from pathlib import Path
import os
from django.utils.translation import get_language
from django.conf import settings
from django.http import HttpResponse
from django.utils import translation as transla

BASE_DIR = Path(__file__).resolve().parent.parent
def translation(arg, arg1, arg2):
    print(arg)
    loader = FluentResourceLoader(os.path.join(BASE_DIR,"blog/l10n/{locale}"))
    lang_list = []  

    user_language = get_language()
    transla.activate('en')
    response = HttpResponse(...)
    response.set_cookie(settings.LANGUAGE_COOKIE_NAME, user_language)  
    if get_language() == 'es':
        lang_list = ['es', 'en']
        pass
    else:
        lang_list = ['en', 'es']
        pass
    print(get_language(), 
          lang_list)
    l10n = FluentLocalization(lang_list, ["main.ftl"], loader)
    val = l10n.format_value(arg, {arg1 : arg2})
    print(val)
    return val


