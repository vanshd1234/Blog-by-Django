from django.db import models

class Signup(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=500)
    confirm_password=models.CharField(max_length=500)
    
    
    def register(self):
        self.save()


    @staticmethod
    def get_customer(email):
        try:
            return Signup.objects.get(email=email)
        except:
            return False