from django import forms
from django.forms.widgets import TextInput, Textarea
from .models import Post

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
            "title": "Titulo",
            "content": "Contenido"
        }

        
        
 