from django.db import models

# Create your models here.
class Person (models.Model):
    Email = models.EmailField(max_length=254)
    password = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.Email