from django.db import models
from django.contrib.auth.models import AbstractUser
from django.template.defaultfilters import slugify

# Create your models here.
class User(AbstractUser):
    pass

    def __str__(self):
        return self.name
    

class Category(models.Model):
    name=models.CharField(max_length=100, unique=True)
    description=models.TextField()
   

    def __str__(self):
        return self.name
    

class ProductImage(models.Model):
    image = models.ImageField(upload_to='additional_images/')

    def __str__(self):
        return self.image.url
    

class Product(models.Model):
    product_id=models.AutoField(primary_key=True,auto_created=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    slug = models.SlugField(null=True,blank=True, unique=True)
    main_image = models.ImageField(upload_to='product_images/', null=True, blank=True)
    additional_images = models.ManyToManyField('ProductImage', related_name='products')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug=slugify(self.name)
        return super().save(*args, **kwargs)
    


class TrendingProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

class MostSoldProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

