from datetime import datetime
from pyexpat import model
from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    phone = models.CharField(max_length=11)
    desc = models.TextField()
    def __str__(self):
        return self.name + " - " + self.phone
       
class Blog(models.Model):
    author_name = models.CharField(max_length=30)
    title = models.CharField(max_length=200)
    tags = models.CharField(max_length=300)
    slug = models.SlugField(max_length=150)
    # prepopulated_fields = {'slug': ('title',)}
    # https://djangocentral.com/building-a-blog-application-with-django/
    photo = models.ImageField(upload_to='media')
    blog = models.TextField()
    published_date = models.DateTimeField(blank=True)
    def __str__(self):
        return self.title + "-" + self.author_name