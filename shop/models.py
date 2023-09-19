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
    
class Brand(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.name
    
class ElectronicsBrand(Brand):
    pass
    

class ClotheBrand(Brand):
    pass


class HomeLivingBrand(Brand):
    pass

class BeautyPersonalCareBrand(Brand):
    pass

class SportsOutdoorsBrand(Brand):
    pass

class ToysGamesBrand(Brand):
    pass
class Colour(models.Model):
    name = models.CharField(max_length=50, unique=True)

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
    colour = models.ForeignKey(Colour, on_delete=models.CASCADE, null=True, blank=True)
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
    
class Electronics(Product):
    size_choices = (
        ('small', 'Small'),
        ('medium', 'Medium'),
        ('large', 'Large'),
    )
    size = models.CharField(max_length=10, choices=size_choices,default='small')
    subCategory_choices = (
        ('computer', 'Computer'),
        ('laptop', 'Laptop'),
        ('phone', 'Phone'),
        ('tablet', 'Tablet'),
        ('accessories', 'accessories'),
    )
    subCategory = models.CharField(max_length=50, choices=subCategory_choices,default='small')
    brand = models.ForeignKey(ElectronicsBrand, on_delete=models.CASCADE, null=True, blank=True)



class ComputerAndPhone(Electronics):
    screen_size = models.CharField(max_length=50)
    processor_type = models.CharField(max_length=100)
    storage_capacity = models.CharField(max_length=100)

class Accessories(Electronics):
    pass
  
class ClotheSize(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name
class Clothe(Product):
    brand = models.ForeignKey(ClotheBrand, on_delete=models.CASCADE, null=True, blank=True)
    material = models.CharField(max_length=100)
    style = models.CharField(max_length=100)
    season = models.CharField(max_length=50)
    
    sizes = models.ManyToManyField(ClotheSize,blank=True)
    gender_choices = (
        ('men', 'Men'),
        ('women', 'Women'),
        ('kids', 'Kids'),
    )
    gender = models.CharField(max_length=10, choices=gender_choices, default='men')

   


class HomeLiving(Product):
    brand = models.ForeignKey(HomeLivingBrand, on_delete=models.CASCADE, null=True, blank=True)
    room_type = models.CharField(max_length=100)
    material = models.CharField(max_length=100)
    dimensions = models.CharField(max_length=100)


class BeautyPersonalCare(Product):
    brand = models.ForeignKey(BeautyPersonalCareBrand, on_delete=models.CASCADE, null=True, blank=True)
    SKIN_TYPES = [
        ('normal', 'Normal'),
        ('dry', 'Dry'),
        ('oily', 'Oily'),
        ('combination', 'Combination'),
        ('sensitive', 'Sensitive'),
    ]

    skin_type = models.CharField(max_length=20, choices=SKIN_TYPES, default='normal')
    fragrance_type = models.CharField(max_length=100)


class SportsOutdoors(Product):
    brand = models.ForeignKey(SportsOutdoorsBrand, on_delete=models.CASCADE, null=True, blank=True)
    sport_type = models.CharField(max_length=100)



class ToysGames(Product):
    brand = models.ForeignKey(SportsOutdoorsBrand, on_delete=models.CASCADE, null=True, blank=True)
    age_group = models.CharField(max_length=50)
    skill_level = models.CharField(max_length=50)


class TrendingProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

class MostSoldProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

