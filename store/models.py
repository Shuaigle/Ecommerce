from django.db import models

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
    # reference to Category table, must have category or will delete cascade
    category = models.ForeignKey(Category, related_name='product', on_delete=models.CASCADE)
    # who actually made this product, connect to User table
    # when delete User table units, will also delete Pruduct table
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='product_creator')
    title = models.CharField(max_length=255)
    # this is author of the book
    author = models.CharField(max_length=255, default='admin')
    # textfield is much larger than Charfield
    description = models.TextField(blank=True)
    # not necessary to put image here, because we can use another table like album table
    image = models.ImageField(upload_to='images/')
    