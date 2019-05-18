from django.urls import path
from .views import *

urlpatterns=[
	path('',t,name="home_url"),
	path('post/<str:slug>/', post_detail, name='post_detail_url')

]
