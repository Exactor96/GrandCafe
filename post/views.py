from django.shortcuts import render
from .models import Post, Tag, Human
from django.views.generic.base import View
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import logout,login
from django.http import HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator
from django.db.models import F
from .forms import PostForm
from uuslug import slugify
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

	success_url = "/recepts/"
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
	Post.objects.filter(slug__iexact=slug).update(views=F('views')+1)
	return render(request, 'post/post_detail.html',context={'post':post})

def add_post(request):
    print(request)
    print(dir(request))
    print(*request.POST)
    print(request.method)
    if request.method == "POST":
        form = PostForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            post = form.save(commit=False)
            post.title = request.POST["title"]
            post.slug = slugify(request.POST["title"])
            link=slugify(request.POST["title"])
            #post.category = category.filter(id__iexact=request.POST["category"]).get('name')
            #post.tags = request.POST["tags"]
            post.ingredients = request.POST["ingredients"]
            post.cooking = request.POST["cooking"]
            post.time_cooking = request.POST["time_cooking"]
            post.save()
            return HttpResponseRedirect("/"+link)
    else:
        form = PostForm()
    return render(request, 'post/add.html', {'form': form})

def post_tags(request):
	tags = Tag.objects.all()
	return render(request, 'post/tag_post.html',context={'tags':tags})
