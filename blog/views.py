from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect

from django.utils import timezone
from datetime import datetime
from .models import Post, Comment
from django.contrib.auth.forms import AuthenticationForm
from .forms import PostForm, CommentForm
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
            return redirect('go_to_administration')
    context = {'form': form}
    return render(request, 'CRUD/form.html', context)


def updatePost(request, pk):
    post = Post.objects.get(id=pk)
    form = PostForm(instance=post)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            print("Article is posted")
            return redirect('go_to_administration')
    context = {'form': form}
    return render(request, 'CRUD/form.html', context)


def deletePost(request, pk):
    post = Post.objects.get(id=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('go_to_administration')
    context = {'item': post}
    return render(request, 'CRUD/delete.html', context)


def add_comment(request, pk):
    thePost = Post.objects.get(id=pk)

    form = CommentForm(instance=thePost)

    if request.method == 'POST':
        form = CommentForm(request.POST, instance=thePost)
        if form.is_valid():
            name = request.user.username
            body = form.cleaned_data['body']
            c = Comment(post = thePost, name=name, body=body, commented_date=datetime.now())
            c.save()
            return redirect('/')
        else:
            print('form is invalid')
    else:
        form = CommentForm()
    context = {'form': form}
    return render(request, 'blog/add_comment.html', context)

def delete_comment(request, pk):
    theComment = Comment.objects.filter(post=pk).last()
    post_id= theComment.post.id
    theComment.delete()
    return redirect('/')