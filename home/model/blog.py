from django.db import models
from .category import Category
class Blog(models.Model):
    email=models.EmailField(max_length=100, default="example@gmail.com")
    title=models.CharField(max_length=50)
    post=models.CharField(max_length=500, default='')
    category=models.CharField(max_length=100)
    
    def reg(self):
        self.save()

    @staticmethod
    def get_all_blogs():
        return Blog.objects.all()

    @staticmethod
    def get_all_blog_by_name(category_name):
        if category_name:
            return Blog.objects.filter(category=category_name)
        else:
            return Blog.get_all_products()