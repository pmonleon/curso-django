from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import View, UpdateView, DeleteView
# from django.views.generic.detail import DetailView

from blog.models import Post
from .forms import PostCreateForm
from django.urls import reverse_lazy
from django.utils.translation import get_language
from blog.ftl_bundles import main as main_bundle
from django_ftl import activate

# Create your views here.
class BlogListView(View):
    """Vista ppal del blog"""
    def get(self, request, *args, **kwargs):
        posts=Post.objects.all()
        context = {
            "posts":posts
        }
        return render(request, 'blog_list.html', context)

class BlogCreateView(View):
    """Vista Post del blog"""
    
    def get(self, request, *args, **kwargs):
        form = PostCreateForm()
        context = {
            "form":form
        }
        print('desde fluent', get_language())
        # sactivate(get_language())
        return render(request, 'blog_create.html', context)
    
    def post(self, request, *args, **kwargs):
        if request.method=='POST':
           form = PostCreateForm(request.POST)
           if form.is_valid():
                # obtener info del form
                title=form.cleaned_data.get('title')
                content=form.cleaned_data.get('content')
                # hacer el post
                p, created=Post.objects.get_or_create(title=title, content=content)
                #p.save
                return redirect('blog:home')
            
        context = {
            
        }
        return render(request, 'blog_create.html', context)

class BlogDetailView(View):
      """Vista Detalle del post"""
      def get(self, request, pk, *args, **kwargs):
          post = get_object_or_404(Post,pk=pk)
          context = {
              "post": post,
              "ftl_bundle": main_bundle
          }
          return render(request, 'blog_detail.html', context)

# myapp.views



# class BlogDetailView(DetailView):
#     model = Post
#     template_name = "blog_detail.html"
    
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['now'] = timezone.now()
    #     return context

     
class BlogUpdateView(UpdateView):
    model = Post
    fields = ['title', 'content']
    template_name = "blog_update.html"
    
    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse_lazy('blog:detail', kwargs={'pk':pk})
    
class BlogDeleteView(DeleteView):
    model = Post
    template_name = "blog_delete.html"
    
    def get_success_url(self):
        return reverse_lazy('blog:home')

    

    

     

    
  


        