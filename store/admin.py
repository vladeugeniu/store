from django.contrib import admin
from .models import Category, Book, Sell, Buy


admin.site.register(Category)
admin.site.register(Book)
admin.site.register(Sell)
admin.site.register(Buy)