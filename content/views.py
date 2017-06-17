from rest_framework import status
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ContentSerializer, CategorySerializer
from .models import *

class list_content(generics.ListAPIView):
    serializer_class = ContentSerializer
    def get_queryset(self):
        return Content.objects.order_by('-posted',).all()

class list_category(generics.ListAPIView):
    serializer_class = CategorySerializer
    def get_queryset(self):
        return Content.objects.order_by('slug',).all()

class content_by_slug(generics.ListAPIView):
    serializer_class = ContentSerializer
    def get_queryset(self):
        slug = self.kwargs['slug']
        return Content.objects.filter(slug=slug)

class content_by_category(generics.ListAPIView):
    serializer_class = ContentSerializer
    def get_queryset(self):
        category = self.kwargs['category']
        id = Category.objects.filter(slug=category)
        return Content.objects.order_by('-posted',).filter(category=id)


