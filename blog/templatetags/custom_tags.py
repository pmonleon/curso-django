"""
    [simple tag] : processes the data and return a string
    [inclusion_tag] : processes the data and return a renderer template
"""

from django import template
from blog.models import Post
from fluent.runtime import FluentLocalization, FluentResourceLoader
from blog.config import translation

from pathlib import Path
import os

register = template.Library()


BASE_DIR = Path(__file__).resolve().parent.parent

@register.simple_tag
def posts_counter():
    return Post.objects.count()

@register.simple_tag
def fname():
    return translation('lista', ['es', 'en'])
    # loader = FluentResourceLoader(os.path.join(BASE_DIR,"blog/l10n/{locale}"))
    # print(loader)
    # l10n = FluentLocalization(["es", "en"], ["main.ftl"], loader)
    # print(l10n)
    # val = l10n.format_value('trial')
    # print('trial', val)
    # return val

print('yeeeeeeeeee', translation('lista', ['es', 'en']))






    