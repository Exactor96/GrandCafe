from django.urls import path
from .views import *

urlpatterns=[
#post root
	path('',h, name="h_url"), #<---post root
	path('page/',paginator, name="home_url"), #<---/post/page
	path('page/<str:slug>/', post_detail, name='post_detail_url'), #/post/page/ReCept Slug
	path('tags/', post_tags, name='post_tags_url')# /post/tags

]
# no slash before path!11111
