from blog.ftl_bundles import main as ftl_bundle

from django.utils.translation import get_language

def translation(arg, arg1, arg2):
    print("calling translation with ", arg, arg1, arg2, get_language())
    val = ftl_bundle.format(arg, {arg1 : arg2})
    return val