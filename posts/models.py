from django.db import models


class Categories(models.Model):
    title = models.CharField(max_length=36)


class Product(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField()
    description = models.TextField(max_length=255)
    price = models.IntegerField()
    created_at = models.DateTimeField(auto_now=True)
    modified_date = models.DateTimeField(auto_now_add=True)

    categories = models.ManyToManyField(Categories)

    @property
    def categories_list(self) -> list:
        return self.categories.all()
