from django.shortcuts import render

# Create your views here.

def t(request):
	return render(request,'post/index.html')
