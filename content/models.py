from django.db import models
from django.db.models import permalink

# Create your models here.
CONTENT_TYPE = (
    ('blog', 'Blog Post'),
    ('project', 'Project'),
)


class Content(models.Model):
    purpose = models.CharField(max_length=10, choices=CONTENT_TYPE)
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    body = models.TextField()
    posted = models.DateTimeField(db_index=True, auto_now_add=True)
    category = models.ForeignKey('content.Category',blank=True,null=True)

    def __str__(self):
        return '%s, %s' % (self.purpose, self.title)

    @permalink
    def get_absolute_url(self):
        return ('view_post', None, { 'slug': self.slug })
    
class Category(models.Model):
    slug = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return '%s' % self.slug

    @permalink
    def get_absolute_url(self):
        return ('view_category', None, { 'slug': self.slug })




