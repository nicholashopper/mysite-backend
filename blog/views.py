from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import BlogSerializer, CategorySerializer
from .models import Blog, Category

@api_view(['GET', 'POST'])
def blog_list(request):
    if request.method == 'GET':
        blogs = Blog.objects.all()
        serializer = BlogSerializer(blogs, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def category_list(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
