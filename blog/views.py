from django.shortcuts import render, get_object_or_404, redirect

from django.utils import timezone

from .models import Post
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
def post_list_index(request):
    post_list = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')

    return render(request, 'blog/post_list.html', {'posts' : post_list})

def post_detail(request, pk):
    post_detail = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post_detail})


