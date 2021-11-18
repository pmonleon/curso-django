from fluent.runtime import FluentLocalization, FluentResourceLoader
from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent
def translation(arg,lista):
    loader = FluentResourceLoader(os.path.join(BASE_DIR,"blog/l10n/{locale}"))
    l10n = FluentLocalization(lista, ["main.ftl"], loader)
    val = l10n.format_value(arg)
    print('ewfwrwewetwets', val)
    return val


print(os.path.join(BASE_DIR,'blog'))
print(translation('welcome', ['es']))