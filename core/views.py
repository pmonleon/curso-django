from django.views.generic import View
from django.shortcuts import render, redirect

from django.utils.translation import activate, get_language_info, get_language


class HomeView(View):
    def get(self, request, *args, **kwargs):
       
        context = {
            
        }
        print('home view', get_language())
        return render(request, 'index.html', context)