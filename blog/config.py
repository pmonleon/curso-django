from fluent.runtime import FluentLocalization, FluentResourceLoader
from pathlib import Path
import os
from django.utils.translation import get_language
f

BASE_DIR = Path(__file__).resolve().parent.parent
def translation(arg, arg1, arg2):
    print(arg)
    loader = FluentResourceLoader(os.path.join(BASE_DIR,"blog/l10n/{locale}"))

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


from fluent_octopus.fluent_service import FluentService
from django.utils.translation import get_language


# def translation(arg):
#     print("calling translation with ", arg)
#     trans_service = FluentService()
#     val = trans_service.get_l10n(get_language()).format_value(arg)
#     print('ewfwrwewetwets', val)
#     return val



