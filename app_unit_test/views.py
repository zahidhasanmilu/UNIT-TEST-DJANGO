from django.shortcuts import redirect, render
from django.http import HttpResponse

from app_unit_test.models import Category, Blog
from app_unit_test.forms import BlogForm

# Create your views here.


def index(request):
    return render(request, 'index.html')


def blogs_list(request):
    blogs = Blog.objects.all().select_related('author', 'category')

    context = {
        'blogs': blogs
    }
    return render(request, 'blogs_list.html', context)


def blog_detail(request, slug):
    blog = Blog.objects.get(slug=slug)
    context = {
        'blog': blog
    }
    return render(request, 'blog_detail.html', context)


def create_blog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.author = request.user  # Assuming the user is logged in
            obj.save()
            return redirect('blog_detail', slug=obj.slug)
    else:
        form = BlogForm()

    context = {
        'form': form
    }
    return render(request, 'create_blog.html', context)


def blog_update(request, slug):
    blog = Blog.objects.get(slug=slug)
    if blog.author != request.user:
        return HttpResponse("You are not authorized to edit this blog.", status=403)
    
    if request.method == 'POST':
        form = BlogForm(request.POST, instance=blog)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.author = request.user  # Assuming the user is logged in
            obj.save()
            return redirect('blog_detail', slug=blog.slug)
    else:
        form = BlogForm(instance=blog)

    context = {
        'form': form,
        'blog': blog
    }
    return render(request, 'blog_update.html', context)



def blog_delete(request, slug):    
    blog = Blog.objects.get(slug=slug)
    if blog.author != request.user:
        return HttpResponse("You are not authorized to delete this blog.", status=403)
    
    blog.delete()
    return redirect('blogs_list')