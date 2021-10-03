from django.shortcuts import render
from django.utils import timezone

from .models import Post

def post_list_index(request):
    post_list = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')

    return render(request, 'blog/post_list.html', {'posts' : post_list})