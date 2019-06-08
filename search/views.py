from django.shortcuts import render
from django.shortcuts import render_to_response
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.views.generic.base import View
from post.models import Post
from . import views
# Create your views here.
class ESearchView(View):
    template_name = 'search/result.html'

    def get(self, request, *args, **kwargs):
        context = {}

        question = request.GET.get('q')
        if question is not None:
            search_posts = Post.objects.filter(title__contains=question)

            # forming a URL string that will contain the last request.
            # This is important for correct operation of pagination
            context['last_question'] = '?q=%s' % question

            current_page = Paginator(search_posts, 10)

            page = request.GET.get('page')
            try:
                context['post_lists'] = current_page.page(page)
            except PageNotAnInteger:
                context['post_lists'] = current_page.page(1)
            except EmptyPage:
                context['post_lists'] = current_page.page(current_page.num_pages)

        return render_to_response(template_name=self.template_name, context=context)

def search(req):
	return render(req,'search/search.html')
