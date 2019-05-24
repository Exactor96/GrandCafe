from django.shortcuts import render
from .models import Post, Tag, Human
from django.views.generic.base import View
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout
from django.contrib.auth import login
from django.http import HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator
# Create your views here.


def greet(request):
	return render(request,'post/greet.html')

class MainView(TemplateView):
	template_name = 'post/blank.html'
	def get(self, request):
		if request.user.is_authenticated:
			humans = Human.objects.all()
			ctx = {}
			ctx['humans'] = humans
			return render(request, self.template_name, ctx)
		else:
			return render(request, self.template_name, {})

class RegisterFormView(FormView):
	form_class = UserCreationForm
	success_url = "/post/login/"

	template_name = "post/register.html"


	def form_valid(self, form):
		form.save()
		return super(RegisterFormView, self).form_valid(form)
	def form_invalid(self, form):

		return super(RegisterFormView, self).form_invalid(form)

class LoginFormView(FormView):
	form_class = AuthenticationForm

	template_name = "post/login.html"

	success_url = "/post/page/"
	def form_valid(self, form):
		self.user = form.get_user()

		login(self.request, self.user)
		return super(LoginFormView, self).form_valid(form)

class LogoutView(View):
	def get(self, request):
		logout(request)
		return HttpResponseRedirect("/")





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
