from django import forms
from django.forms.widgets import TextInput, Textarea
from .models import Post
from django.utils.translation import get_language
# from blog.config import translation
from fluent_octopus.fluent_service import translation
from blog.ftl_bundles import main as ftl_bundle

class PostCreateForm(forms.ModelForm):
    """docstring for PostCreateForm."""
    class Meta:
        model=Post
        fields=('title', 'content')
        widgets = {
            "title" : TextInput(attrs={"placeholder" :  ftl_bundle.format_lazy("place")}),
            "content" : Textarea(attrs={"placeholder" : translation("placeholder_content", "", "")})
        }
        labels = {
            "title": translation("create_titulo", "", ""),
            "content": translation("create_contenido", "", ""),
        }
        print('idioma', get_language())

        
        
 