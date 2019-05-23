from django.shortcuts import render
from .models import Post, Tag
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.core.paginator import Paginator
# Create your views here.




def h(request):
	return render(request,'post/blank.html')

def paginator(request):
	posts = Post.objects.all()
	paginator = Paginator(posts, 10)

	page_number = request.GET.get('page', 1)
	page = paginator.get_page(page_number)


	is_paginated = page.has_other_pages()
	if page.has_previous():
		prev_url='?page={}'.format(page.previous_page_number())
	else:
		prev_url = ''

	if page.has_next():
		next_url='?page={}'.format(page.next_page_number())
	else:
		next_url=''
	context= {'page_object':page,
	             'is_paginated':is_paginated,
				 'next_url':next_url,
				 'prev_url':prev_url
	}
	return render(request,'post/index.html', context=context)

def post_detail(request, slug):
	post = Post.objects.get(slug__iexact=slug)
	return render(request, 'post/post_detail.html',context={'post':post})

def post_tags(request):
	tags = Tag.objects.all()
	return render(request, 'post/tag_post.html',context={'tags':tags})
