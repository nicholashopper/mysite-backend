from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = {
    url(r'^api/getAllBlogs$', views.blog_list),
    url(r'^api/getAllCategories$', views.category_list),
}

urlpatterns = format_suffix_patterns(urlpatterns)
