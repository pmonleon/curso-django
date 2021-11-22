from django import forms
from django.forms.widgets import TextInput, Textarea
from .models import Post
from django.utils.translation import get_language
from blog.config import translation

class PostCreateForm(forms.ModelForm):
    """docstring for PostCreateForm."""
    class Meta:
        model=Post
        fields=('title', 'content')
        widgets = {
            "title" : TextInput(attrs={"placeholder" : "añade un titulo"}),
            "content" : Textarea(attrs={"placeholder" : "añade un comentario"})
        }
        labels = {
            "title": translation("create_titulo", "", ""),
            "content": translation("create_contenido", "", ""),
        }
        print('idioma', get_language())

        
        
 