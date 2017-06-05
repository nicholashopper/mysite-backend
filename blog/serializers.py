from rest_framework import serializers
from .models import Blog, Category

class BlogSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Blog
        fields = ('title', 'slug', 'body', 'posted', 'category')

class CategorySerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""
         
    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Category
        fields = ('title', 'slug')
