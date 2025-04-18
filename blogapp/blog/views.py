from django.http.response import HttpResponse
from django.shortcuts import render
from blog.models import Blog, Category, Services


def index(request):
    context = {
        "blogs": Blog.objects.filter(is_active=True),
        "categories": Category.objects.all(),
        "services": Services.objects.all(),
    }
    return render(request, "blog/index.html", context)

def blogs(request):
    context = {
        "blogs": Blog.objects.filter(is_active=True),
        "categories": Category.objects.all()
    }
    return render(request, "blog/blogs.html", context)

def blog_details(request, slug):
    blog = Blog.objects.get(slug=slug)
    return render(request, "blog/blog-details.html", {
        "blog": blog
    })
    
def references(request):
    context = {
    "services": Services.objects.all(),
    }
    return render(request, "blog/prefetences.html", context)

def contact(request):
    context = {
    "services": Services.objects.all(),
    }
    return render(request, "blog/contact.html", context)

def about(request):
    context = {
    "services": Services.objects.all(),
    }
    return render(request, "blog/about.html", context)


def services(request):
      context = {
        "blogs": Services.objects.filter(is_active=True),
        "services": Services.objects.all(),
      }
      return render(request, "blog/services.html", context)

def service_details(request, slug):
    blog = Services.objects.get(slug=slug)
    return render(request, "blog/services-details.html", {
        "blog": blog,
        "services": Services.objects.all(),
    })

def blogs_by_category(request, slug):
    context = {
        "blogs": Category.objects.get(slug=slug).blog_set.filter(is_active=True),
        "categories": Category.objects.all(),
        "selected_category": slug
    }
    return render(request, "blog/blogs.html", context)