from django.urls import path
from .views import HomePageView, ListBlogsView, BlogDetailView


app_name = 'blog'

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('blogs/', ListBlogsView.as_view(), name='blogs'),
    path('blog/<slug:slug>/', BlogDetailView.as_view(), name='blog_detail'),
]