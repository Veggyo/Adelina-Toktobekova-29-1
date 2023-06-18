from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField()
    description = models.TextField(max_length=255)
    price = models.IntegerField()
    created_at = models.DateTimeField(auto_now=True)
    modified_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title



