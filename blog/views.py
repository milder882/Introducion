from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import View, UpdateView, DeleteView


class BlogListView(View):
    def get(self, request, *args, **kwargs):
        context={
            
        }
        return render(request, 'blog_list.html', context)
