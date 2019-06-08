from django.urls import path
from .views import *
from . import views

urlpatterns = [
    # post root
    #path('register/', views.RegisterFormView.as_view()),
    #path('login/', views.LoginFormView.as_view()),
    #path('logout/', views.LogoutView.as_view()),
    path(r'', views.MainView.as_view()),  # <---post root
    #path('recepts/', paginator, name="home_url"),  # <---/post/page
    path('recept/<str:slug>/', post_detail, name='post_detail_url'),  # /post/page/ReCept Slug
    path('tags/', post_tags, name='post_tags_url'),
    


]
# no slash before path!11111
