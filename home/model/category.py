from django.db import models
# Create your models here.


class Category(models.Model):
    name=models.CharField(max_length=20)


    @staticmethod
    def get_all_categories():
        return Category.objects.all()