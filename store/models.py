from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse



# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, unique=True)

    # we can override django default setting by class Meta
    class Meta:
        verbose_name_plural = 'categories'

    # parameter
    def get_absolute_url(self):
        return reverse("store:category_list", args=[self.slug])

    def __str__(self) -> str:
        return self.name

class Product(models.Model):
    # reference to Category table, must have category or will delete cascade, important
    category = models.ForeignKey(Category, related_name='product', on_delete=models.CASCADE)
    # who actually made this product, connect to User table
    # when delete User table units, will also delete Pruduct table
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='product_creator')
    title = models.CharField(max_length=255)
    # this is author of the book
    author = models.CharField(max_length=255, default='admin')
    # textfield is much larger than Charfield
    description = models.TextField(blank=True)
    # not necessary to put image here, because we can use another table like album table in media folder
    image = models.ImageField(upload_to='images/')
    # urls last unique place that we can utilize it
    slug = models.SlugField(max_length=255)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    in_stock = models.BooleanField(default=True)
    # products that are active to buy
    is_active = models.BooleanField(default=True)
    # auto_now_add is going to happen only once
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name_plural = 'Products'
        # '-created' will show the latest created product first
        # 'created' will reverse
        ordering = ('-created',)

    def __str__(self) -> str:
        return self.title