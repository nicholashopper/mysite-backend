from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = {
    url(r'^content$', views.list_content.as_view()),
    url(r'^category$', views.list_category.as_view()),
    url(r'^content/slug-(?P<slug>.+)/$', views.content_by_slug.as_view()),
    url(r'^content/category-(?P<category>.+)/$', views.content_by_category.as_view()),
}

urlpatterns = format_suffix_patterns(urlpatterns)
