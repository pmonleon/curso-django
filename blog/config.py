from fluent.runtime import FluentLocalization, FluentResourceLoader
from pathlib import Path
import os
from fluent_octopus.fluent_service import FluentService
from django.utils.translation import get_language


def translation(arg):
    print("calling translation with ", arg)
    trans_service = FluentService()
    val = trans_service.get_l10n(get_language()).format_value(arg)
    print('ewfwrwewetwets', val)
    return val


print(translation('welcome'))
