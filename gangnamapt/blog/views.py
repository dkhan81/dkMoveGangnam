from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect

# Create your views here.
from .models import Post, Test, Resume
from django.utils import timezone
from .forms import PostForm
from django.contrib.auth.decorators import login_required


def post_list(request):
    posts = Resume.objects.all().order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

'''
def note(request): 
    note = Test.objects.all().order_by('-published_date')
    return render(request, 'simple/note.html', {'note' : note})
'''

@login_required
def post_detail(request, pk) :
    post = get_object_or_404(Resume, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

@login_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            # post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

@login_required
def post_edit(request, pk):
    post = get_object_or_404(Resume, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            # post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

def post_draft_list(request):
    posts = Resume.objects.filter(published_date__isnull=True).order_by('created_date')
    return render(request, 'blog/post_draft_list.html', {'posts': posts})

def post_publish(request, pk):
    post = get_object_or_404(Resume, pk=pk)
    post.publish()
    return redirect('post_detail', pk=pk)

def post_remove(request, pk):
    post = get_object_or_404(Resume, pk=pk)
    post.delete()
    return redirect('post_list')