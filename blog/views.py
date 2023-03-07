from django.shortcuts import render
from .models import post
# Create your views here.

def list(request):
    Data = {'posts': post.objects.all().order_by('-date')}
    return render(request, 'pages/blog.html', Data)

def show_post(request, id):
    show_post = post.objects.get(id=id)
    return render(request, 'pages/post.html', {'posts': show_post})