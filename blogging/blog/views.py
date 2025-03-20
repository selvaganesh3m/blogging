from django.core.paginator import Paginator
from django.shortcuts import render
from django.views.generic import TemplateView
from django.views import View
from .models import Blog
from django.views.generic import DetailView




class HomePageView(TemplateView):
    template_name = 'blog/home.html'



class ListBlogsView(View):
    def get(self, request):
        blogs = Blog.objects.filter(is_active=True).order_by('-created_at')
        paginator = Paginator(blogs, 9)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)         
        return render(request,"blog/blogs.html", {'blogs': page_obj}) # {'blogs': blogs } It has to be a blogs like I written but I paginated it so the variable name is changed
    
class BlogDetailView(DetailView):
    model = Blog
    template_name = 'blog/blog_detail.html'
    context_object_name = 'blog'

    def get_queryset(self):
        return Blog.objects.filter(slug=self.kwargs['slug'])