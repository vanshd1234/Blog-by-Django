from django.contrib import admin
from .model import Signup
from .model import Blog
from .model import Category
# Register your models here.
admin.site.register(Signup)
admin.site.register(Blog)
admin.site.register(Category)