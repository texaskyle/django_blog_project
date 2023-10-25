from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.http import HttpResponse
from .models import Post


# Create your views here.
def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']


class PostDetailView(DetailView):
    pass


def about(request):
    return render(request, 'blog/about.html', {'title': 'About page'})


def messages(request):
    return render(request, 'blog/messages.html')


def article(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/article.html', context)