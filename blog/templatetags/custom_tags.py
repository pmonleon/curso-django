"""
    [simple tag] : processes the data and return a string
    [inclusion_tag] : processes the data and return a renderer template
"""

from django import template
from blog.models import Post
from fluent.runtime import FluentLocalization, FluentResourceLoader
# from blog.config import translation
from fluent_octopus.fluent_service import translation
import html2text
from pathlib import Path

import os

register = template.Library()


BASE_DIR = Path(__file__).resolve().parent.parent

from html.parser import HTMLParser
 
class Parse(HTMLParser):
    def __init__(self):
    #Since Python 3, we need to call the __init__() function 
    #of the parent class
        super().__init__()
        self.reset()
 
    #Defining what the methods should output when called by HTMLParser.
    def handle_starttag(self, tag, attrs):
        print("Start tag: ", tag)
        for a in attrs:
            print("Attributes of the tag: ", a)
 
    def handle_data(self, data):
        print("Here's the data: ", data)
 
    def handle_endtag(self, tag):
        print("End tag: ", tag)  

@register.simple_tag
def posts_counter():
    return Post.objects.count()

@register.simple_tag
def fname(trans_string, arg1, arg2):
    if arg1 == "" and arg2 == "":
        return translation(trans_string, "", "")
    else:
        if  trans_string == 'crear-label':
            testParser = Parse()
            testParser.feed(arg2)
            if 'title' in arg2:
                arg2 = 'titulo'
                pass
            elif 'content' in arg2:
                arg2 = 'contenido'
                pass
            else:
                arg2
        
        
        print('htmlparser', arg1, arg2)
        return translation(trans_string, arg1, arg2)
    # loader = FluentResourceLoader(os.path.join(BASE_DIR,"blog/l10n/{locale}"))
    # print(loader)
    # l10n = FluentLocalization(["es", "en"], ["main.ftl"], loader)
    # print(l10n)
    # val = l10n.format_value('trial')
    # print('trial', val)
    # return val


@register.simple_tag
def htmlTrans(trans_html):
    print('imprime',html2text.html2text(trans_html))
    return ''





    