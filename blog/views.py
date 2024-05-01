from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import Post
from django.views.generic import ListView, CreateView, DetailView
from .forms import PostForm
from django.urls import reverse_lazy

def get(request):
    post_objs = Post.objects.all()
    context = {
        "posts": post_objs
    }
    return render(request, 'blog/post_list.html', context)

class Detail(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'
    
class Write(CreateView):
    model = Post
    form_class = PostForm
    success_url = reverse_lazy('blog:list')
    



