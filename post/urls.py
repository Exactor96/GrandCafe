from django.urls import path
from .views import *
from . import views

urlpatterns=[
#post root
	path(r'', views.MainView.as_view()), #<---post root
	path('page/',paginator, name="home_url"), #<---/post/page
	path('page/<str:slug>/', post_detail, name='post_detail_url'), #/post/page/ReCept Slug
	path('tags/', post_tags, name='post_tags_url'),
	path('add/',views.MainView.as_view)

]
# no slash before path!11111
