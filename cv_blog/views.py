from django.shortcuts import render, get_object_or_404
from .models import Blog
from django.views.generic import ListView, DetailView


class BlogList(ListView):
    template_name = 'blog_page.html'
    paginate_by = 6
    model = Blog


class DetailPost(DetailView):
    template_name = 'detail_page.html'

    def get_object(self):
        pk = self.kwargs.get('pk')
        return get_object_or_404(Blog, id=pk)
