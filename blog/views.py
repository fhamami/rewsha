#from django.template import RequestContext
from django.shortcuts import get_object_or_404, render
from django.template import RequestContext
from blog.models import Category, Post

def home(request):
	post = Post.objects.all()[:10]
	data = {
		'blog' : post
	}
	return render(request, 'index.html', data)

def detail(request, slug):
	post = Post.objects.get(slug=slug)
	data = {
		'post' : post
	}
	return render(request, 'post.html', data)