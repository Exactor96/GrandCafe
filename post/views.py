from django.shortcuts import render

from .models import Post
# Create your views here.

def t(request):
	posts = Post.objects.all()
	return render(request,'post/index.html', context={'posts':posts})
def post_detail(request, slug):
	post = Post.objects.get(slug__iexact=slug)
	return render(request, 'post/post_detail.html',context={'post':post})
