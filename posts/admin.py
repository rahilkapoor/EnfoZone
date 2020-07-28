from django.contrib import admin
# Register your models here.
from .models import Author, Post, Category

admin.site.register(Author)
admin.site.register(Post)
admin.site.register(Category)
