from django.shortcuts import render

from .models import Blog  

def blog(request):
    blogs = Blog.objects.all()
    context = {
        'blogs': blogs 
    }
   
    return render(request, 'blog.html', context)
