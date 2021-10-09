from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect

from django.utils import timezone
from .models import Post
from django.contrib.auth.forms import AuthenticationForm
from .forms import PostForm
from django.contrib.auth import login
def post_list_index(request):
    post_list = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')

    return render(request, 'blog/post_list.html', {'posts' : post_list})

def post_detail(request, pk):
    post_detail = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post_detail})


def go_to_administration(request):
    post_list = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'CRUD/index.html', {'posts':post_list})
### CRUD

def createPost(request):
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            print("Article is posted")
            return redirect('/')
    context = {'form': form}
    return render(request, 'CRUD/form.html', context)



def delete(request, id):
    obj = Post.objects.get(pk=id)
    obj.delete()
    return HttpResponseRedirect('accounts/manage_articles')
